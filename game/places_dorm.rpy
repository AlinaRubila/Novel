label Kitchen:
    mc "Можете показать, где тут кухня?"

    od "Хорошо, пойдём."

    stop background
    stop music
    scene black with dissolve

    play sound steps

    play music room

    scene black with dissolve

    scene bg_kitchen_evening with dissolve
    play music home
    play background room

    "Кухня была прямо рядом с моей комнатой. Довольно выгодное расположение, так как не придётся протаптывать целый коридор, чтобы просто разогреть ужин в микроволновке."

    "А если она ещё и окажется занята, то это вообще туши свет."

    "На самой кухне в воздухе висел приятный аромат: видимо, кто-то пожарил себе мясо."

    "Сбоку стояла электрическая плита, местами запачканная. Мне сказали, что убираются на кухне сами студенты чётко по графику. Но, судя по окружающим издержкам готовки, сегодня дежурства пока не было."

    "Справа от плиты находился стол с микроволновкой, а под ним было уже почти полностью забитое мусорное ведро. Мусор выносят так же по графику."

    "Над микроволновкой для особо одарённых висели правила по её использованию. Однако, как ни странно, кто-то умудрялся их нарушать."

    "У другой стены были две раковины, большие, как мойдодыр. В одной из них текла только холодная вода, поэтому спрос на первую был в разы больше."

    show comenda home normala at right2 with dissolve

    od "В холодильнике полки поделены между жильцами. Кстати, с плитой будь осторожнее, она долго разогревается."

    show mc normala at left2 with dissolve
    mc "Хорошо, я понял. Спасибо, что предупредили."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm

label Dayroom:
    mc "В общежитии есть комната отдыха?"

    od "Да, она находится на втором этаже."

    stop background
    stop music
    scene black with dissolve

    play sound steps

    play background room

    scene bg_dayroom with dissolve

    "Комната отдыха располагалась недалеко. Нужно было свернуть за угол и пройти через дверь в конце коридора, чтобы оказаться в ней."

    "Комната отдыха оказалась не такой захламленной, какой могла быть."

    "В центре стояли столы, рядом с ними были кресла-груши и стулья, а на стенах висели стеллажи с никому уже не нужными книгами и настольными играми, в которых отсутствовало большинство составляющих."

    "Единственным, что привлекало внимание, были стены этой комнаты, покрытые фотографиями, рисунками и парой плакатов с правилами дорожного движения и проживания в общежитии, на которых вместо привычных всем детишек и животных был изображён персонаж какого-то аниме."

    "Видимо, автор этих художеств был фанатом японской мультипликации."
    show comenda home normala at right2 with dissolve

    od "В комнате отдыха нельзя мусорить. Сидеть ночью можно, но главное тихо."
    show mc smilea at left2 with dissolve

    mc "Ого. А здесь классно."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm
label Laundry:
    mc "Где здесь можно постирать вещи?"

    od "На первом этаже у нас стоят стиральные машины."

    stop music
    stop background

    scene black with dissolve
    play sound steps

    play background room

    scene bg_laundry with dissolve

    "Ольга Дмитриевна провела меня по первому этажу нашего общежития."

    "Справа и слева располагались двери, которые вели в комнаты живущих там студентов. Но на одной из них было написано «Постирочная»."

    "Комендант прошла со мной в помещение, где стояло пять стиральных машин, а сверху над ними были сушилки для белья. Мне кажется, это довольно удобно. Жаль, конечно, что стиралка не в комнате, но то, что она хотя бы есть, не может не радовать."

    show comenda home normala at right2 with dissolve

    od "Тут вещи можно и постирать, и погладить. Не забывай после себя всё выключать. Стиральный порошок каждый покупает свой. Хранить его можно здесь."

    "Она указала на шкаф напротив."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm
