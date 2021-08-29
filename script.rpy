# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("setumi",ctc="ctc_animation",ctc_position= "nestled", ctc_pause="ctc_animation", ctc_timedpause="ctc_animation")
define nl = Character(" ",ctc="ctc_animation",ctc_position= "nestled", ctc_pause="ctc_animation", ctc_timedpause="ctc_animation")

init -2:
    screen _ctc:
        if not _preferences.afm_enable:
            add ctc


image ctc_animation: # CTC
    xalign 0.5 yalign 0.5
    "gui/ctc.png" with Dissolve(2.0,alpha=True)
    2.0
    "gui/ctc_1.png" with Dissolve(2.0,alpha=True)
    2.0
    repeat

image c00:
    "bg/e/c00.png"
    #im.Crop("bg/c00.png", (0, 112.5, 800, 375))
    xsize 1280
    ysize 960
    yanchor 0.8

image byoin7_rouka:
    "bg/e/byoin7_rouka.png"
    #im.Crop("bg/c00.png", (0, 112.5, 800, 375))
    xsize 1280
    ysize 960
    yanchor .9

image danwa:
    "bg/e/danwa.png"
    #im.Crop("bg/c00.png", (0, 112.5, 800, 375))
    xsize 1280
    ysize 960
    yanchor .9

transform bg_size:
    xsize 1280
    ysize 960
    yanchor .9

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。
    play music "audio/bgm/n04.ogg"

    scene byoin7_rouka with Dissolve(1.0)

    nl "走廊的一侧，护士站的对面，是一个被当做休闲室的地方"


    scene danwa with fade

    nl '''在这间冷清的屋子里，\n
    摆放着几张沙发和折叠椅，以及一台大屏幕电视机。

    ２８英寸的屏幕中，
    还在播放着无聊的新春特别节目。

    有一位女孩子，
    正在漫不经心地看着那无聊的电视节目。

    瘦小的身体，粉红色的睡衣。
    手腕上，佩戴着与我相同的白色手环。

    垂到腰间的长发给我留下了深刻的第一印象。'''

    scene black

    nl '''「我说…这节目有意思吗？」

    我随意问道。

    因为环境太过冷清，身不由己地和她搭上了话。'''

    voice "audio/voice/w/nv011b.ogg"

    nl "「不…」"

    voice sustain

    nl '''女孩简短地回答道。
    甚至没有转头看我一眼。

    她似乎根本没有把我放在心上，
    还是一脸无聊地看着那电视节目。

    …既然这么无聊，还不如别看了…

    尽管心中这样想着，
    但我也同样在折叠椅上坐了下来。

    然后，与她一起傻盯着电视机。
    没有其他事情可做，也没有其他事情能做。'''



    # scene bg room
    #
    # # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # # “eileen happy.png”的文件来将其替换掉。
    #
    # show eileen happy
    #
    # # 此处显示各行对话。
    #
    # e "您已创建一个新的 Ren'Py 游戏。"
    #
    # e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
