players = 9

card_width = 76
card_width_resized = 37

card_height = 106
card_height_resized = 53

# absolute position
table_pos = dict(
    x=720,
    y=160,
    w=1200,
    h=860,
    num=1,
    prefix="table"
)

# relative pos from cropped table img(unmodified size)
my_cards_pos = dict(
    x=519,
    y=545,
    w=card_width,
    h=card_height,
    num=2,
    prefix="hand"
)
# relative pos from cropped table img(half size)
my_cards_pos_resized = dict(
    x=500,
    y=720,
    w=card_width_resized,
    h=card_height_resized,
    num=2
)
# relative pos from cropped table img(unmodified size)
middle_cards_pos = dict(
    x=397,
    y=305,
    w=card_width,
    h=card_height,
    num=5,
    prefix="middle"
)

dchip_w = 50
dchip_h = 50
dealer_chip = [dict() for i in range(players)]
if players == 9:
    dealer_chip[0] = dict(
        x=475,
        y=533,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[1] = dict(
        x=290,
        y=435,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[2] = dict(
        x=218,
        y=319,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[3] = dict(
        x=350,
        y=245,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[4] = dict(
        x=538,
        y=193,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[5] = dict(
        x=771,
        y=214,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[6] = dict(
        x=890,
        y=275,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[7] = dict(
        x=930,
        y=433,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[8] = dict(
        x=792,
        y=492,
        w=dchip_w,
        h=dchip_h
    )
elif players == 3:
    dealer_chip[0] = dict(
        x=445,
        y=520,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[1] = dict(
        x=425,
        y=213,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[2] = dict(
        x=929,
        y=303,
        w=dchip_w,
        h=dchip_h
    )
elif players == 6:
    dealer_chip[0] = dict(
        x=463,
        y=528,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[1] = dict(
        x=225,
        y=400,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[2] = dict(
        x=357,
        y=228,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[3] = dict(
        x=627,
        y=222,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[4] = dict(
        x=918,
        y=290,
        w=dchip_w,
        h=dchip_h
    )
    dealer_chip[5] = dict(
        x=858,
        y=485,
        w=dchip_w,
        h=dchip_h
    )
