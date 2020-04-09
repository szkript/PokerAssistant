# Part 1 - Building the CNN
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import time
from utils import Utils

start_time = time.time()


def new_train():
    # SETTINGS!! here <-
    global_settings = dict(
        number_of_classes=Utils.number_of_training_folders(),
        steps_per_epoch=6000,
        epochs=10,
        validation_steps=600,
        save_model_name="long_classifier.h5"
    )

    # starts from here
    # init classifier model
    classifier = init_new_model(0)

    training_set, test_set = prepare_dataset()

    classifier.fit_generator(
        training_set,
        steps_per_epoch=global_settings["steps_per_epoch"],
        epochs=global_settings["epochs"],
        validation_data=test_set,
        validation_steps=global_settings["validation_steps"],
    )
    # save stuff
    # save model and architecture to single file
    classifier.save(global_settings["save_model_name"])
    print("Saved model to disk")
    time_taken = time.time() - start_time
    print("--- %s seconds ---" % time_taken)
    # tools.job_done_alert()


def continue_training():
    # SETTINGS!! here <-
    global_settings = dict(
        number_of_classes=Utils.number_of_training_folders(),
        steps_per_epoch=500,
        epochs=10,
        validation_steps=5,
        save_model_name="long_classifier.h5"
    )

    classifier = load_model("recognizer/long_classifier.h5")
    # Compiling the CNN
    compile_model(classifier)
    training_set, test_set = prepare_dataset()

    classifier.fit_generator(
        training_set,
        steps_per_epoch=global_settings["steps_per_epoch"],
        epochs=global_settings["epochs"],
        validation_data=test_set,
        validation_steps=global_settings["validation_steps"]
    )
    # save model and architecture to single file
    classifier.save(global_settings["save_model_name"])
    print("Saved model to disk")
    time_taken = time.time() - start_time
    print("--- %s seconds ---" % time_taken)


def init_new_model(model_template_index):
    # todo: model templating for faster experiment
    model_templates = []
    # Initialising the CNN
    classifier = Sequential()

    # Step 1 - Convolution
    classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # Adding a second convulutional layer
    classifier.add(Convolution2D(32, 3, 3, activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # Step 3 - Flattening
    classifier.add(Flatten())
    classifier.add(Dropout(0.5))

    # Step 4 - Full connection
    classifier.add(Dense(output_dim=128, activation='relu'))
    classifier.add(Dense(output_dim=Utils.number_of_training_folders(), activation='softmax'))
    compile_model(classifier)
    return classifier


def compile_model(model):
    # Compiling the CNN
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


def prepare_dataset():
    # Part 2 - Fitting the CNN to the images
    train_datagen = ImageDataGenerator(rescale=1. / 255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                     target_size=(64, 64),
                                                     batch_size=32,
                                                     class_mode='categorical')

    test_set = test_datagen.flow_from_directory('dataset/test_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='categorical')

    return training_set, test_set


# continue_training()
new_train()
