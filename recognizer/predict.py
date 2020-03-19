from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator


class Predict:
    __MODEL_NAME = "long_classifier.h5"

    classes = None
    classifier = None

    __training_set = None
    __CONFIDENCE = 0.9

    def __init__(self):
        self.__load_my_model()
        self.classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.__prediction_classes()

    def predict(self, image):
        result = self.classifier.predict(image)
        prediction = "nothing"
        for i in range(result.size):
            if result[0][i] >= self.__CONFIDENCE:
                prediction = self.__get_class(i)
                break
        return prediction

    def __load_my_model(self):
        # load model
        self.classifier = load_model(self.__MODEL_NAME)
        # summarize model.
        self.classifier.summary()

    def __prediction_classes(self):
        train_datagen = ImageDataGenerator(rescale=1. / 255,
                                           shear_range=0.2,
                                           zoom_range=0.2,
                                           horizontal_flip=True)

        self.__training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                                target_size=(64, 64),
                                                                batch_size=32,
                                                                class_mode='binary')

        self.classes = self.__training_set.class_indices

    def __get_class(self, index):
        for key, value in self.__training_set.class_indices.items():
            if value == index:
                return key
