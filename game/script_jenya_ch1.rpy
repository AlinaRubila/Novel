# Начало первой главы рута Жени

#Переменные этого рута

define cookie = False
define eda = False
define excursion = False
define favorite_food = False
define skolko_mest_na_excursion = 0
define visitCanteen = True
define visitPark = True
define visitLibrary = True
define jenya_excursion = False
define visit1 = False
define visit2 = False
define visit3 = False
define askJenya = False
define askTimur = False
define askAlex = False
define askMargo = False

#Выбор печенья

image bg_classroom = "bg/bg_classroom.png"
image bg_street_d = "bg/bg_street_day.png"
image cookieCG = "coockieChoice/cg_cookie.png"
image cookieYes = "coockieChoice/cg_yescookie.png"
image cookieNo = "coockieChoice/cg_nocookie.png"


image bg_classroom_blur = im.Blur("bg/bg_rutnoeve.png", 1.5)

screen cookieChoice():
    imagebutton:
        xalign 0.600
        yalign 0.676
        auto "images/coockieChoice/cookie_button_%s.png" focus_mask True action [SetVariable("cookie", True), Return(value=None)]
    imagebutton:
        xalign 0.053
        yalign 0.22
        auto "images/coockieChoice/lid_button_%s.png" focus_mask True action [Return(value=None)]

screen guyChoice():
    imagebutton:
        xalign 0.5189
        yalign 0.411
        auto "images/rutChoice/jenya_button_%s.png" focus_mask True action [SetVariable("askJenya", True), Return(value=None)]
    imagebutton:
        xalign 0.7889
        yalign 0.825
        auto "images/rutChoice/alex_button_%s.png" focus_mask True action [SetVariable("askAlex", True), Return(value=None)]
    imagebutton:
        xalign 0.914
        yalign 0.563
        auto "images/rutChoice/timur_button_%s.png" focus_mask True action [SetVariable("askTimur", True), Return(value=None)]
    imagebutton:
        xalign 0.0895
        yalign 0.357
        auto "images/rutChoice/margo_button_%s.png" focus_mask True action [SetVariable("askMargo", True), Return(value=None)]



label jenya_cp1:

    if persistent.ending1 and persistent.ending122:
         scene bg_rut
    else:
        scene bg_rutnoeve


    "Она выглядит дружелюбной."

    "Я направился к рыжеволосой девушке."

    "Она что-то рассматривала в окне. Не знаю, что именно привлекло её внимание, но своим внезапным появлением я её отвлёк."

    "На меня смотрели яркие зелёные глаза, в них горел какой-то задорный огонёк, что не могло не заинтересовать."

    #Другой фон аудитории. Спрайт гг в куртке слева и спрайт Жени справа.

    scene cj_meet_jenya with dissolve

    play music cozy

    mc "Привет, не против, если подсяду?"

    #В диалоговом окне имя Жени не указывается пока что

    scene cj_meet_jenya_smile with dissolve

    un "Привет! Садись, конечно!"

    #Спрайт Жени с широкой улыбкой - c широкой нет
    scene cj_meet_jenya_smile with dissolve



    "Я скинул с себя куртку и положил на сиденье рядом с собой."

    j "Я тебя раньше не видела. Меня, кстати, Женя зовут."

    #Теперь в диалоговом окне указывается имя Жени. Спрайт Жени с обычной улыбкой.

    scene cj_meet_jenya with dissolve

    mc "А меня [mcname], приятно познакомиться!"

    scene cj_meet_jenya_smile with dissolve

    j "Взаимно!"

    #Спрайт Жени с широкой улыбкой
    scene cj_meet_jenya_smile with dissolve

    "Женя широко мне улыбалась, и я понял, что сесть к ней было правильным выбором. Какая-то у неё позитивная энергетика, и человек сразу расположил меня к себе. Думаю, мы даже сможем подружиться."

    #Спрайт Жени, где она смотрит в сторону. Звук шуршания пакета

    scene cj_meet_jenya_search with dissolve

    "Неожиданно Женя отвернулась и принялась копошиться в сумке."

    "Через мгновение я почувствовал приятный запах. Такой аромат у меня сразу ассоциируется с домашним теплом и уютом."

    #Спрайт Жени с печенькой в руках.

    j "Ой, хочешь печеньку?"

    scene cookieCG with dissolve

    "Я задумался."


    call screen cookieChoice
    if cookie:
        scene cookieYes with dissolve

        $ relate_jenya += 5

        #show screen scr_over
        #show screen scr_hider

        mc "Спасибо большое."

        #Спрайт гг с печенькой. Спрайт Жени без печенья с широкой улыбкой

        j "Да не за что!"

        "Из-за того, что опаздывал, не успел даже поесть."

        "Выглядит вкусно."

        "Я откусил печенье, оно быстро таяло во рту, оставляя приятное шоколадное послевкусие."

        "Похожее печенье делала мне моя мама, я его просто обожал."

        "Выпечка была свежей, казалось, что её совсем недавно достали из духовки. Неужели она приготовила его сама?"

        "Я не заметил, как быстро съел угощение. Всё-таки отсутствие завтрака дало о себе знать."



    else:
        scene cookieNo with dissolve

        #Спрайт смущённого гг с рукой за головой

        #show screen scr_over
        scene bg_rutnoeve with dissolve

        mc "Спасибо, но я откажусь"


        $ relate_jenya -= 5

        #Спрайт с расстроенной Женей, но быстро сменяется вновь на улыбчивую
        show jenya smilea  at right2 with dissolve


        j "Значит мне больше достанется"

        "Ай, ну я же сегодня ещё не ел."

        "В подтверждение моих мыслей у меня вновь заболел живот."

        "Наверное, мне стоило согласиться. И это печенье так аппетитно пахнет."

        "От мыслей о еде меня отвлекла моя новая знакомая."


    scene bg_classroom_blur with dissolve

    show jenya normal smilea at right2 with dissolve

    show mc normala at left2 with dissolve

    j "Слушай, я про стольких одногруппников успела узнать! Хочешь, расскажу?"

    #(этот вопрос не предполагает отказа)

    mc "Давай."

    show jenya thoughtfula at right2 with dissolve

    j "Про кого ты хочешь узнать?"

    #Изображение где видно Тимура, Шнурка, Марго и саму Женю. Игрок может кликнуть на того, про кого хочет узнать
    #После выбора снова на фоне аудитория и спрайт Жени и гг
    #Если есть ещё про кого спросить, то снова появляется изображение с выбором
    if persistent.ending1 and persistent.ending122:
        scene bg_rut with dissolve
    else:
        scene bg_rutnoeve with dissolve





    call screen guyChoice

    if askJenya:

        scene bg_classroom_blur with dissolve
        show jenya smilea at right2 with dissolve
        show mc normala at left2 with dissolve



        j "Поживешь - увидишь. Я крутая."

        show jenya blusha at right2 with dissolve

        j "Это всё."

        n "Женя смущённо отводила взгляд, но по её улыбке я понял, что ей было приятно моё любопытство."

        $ relate_jenya += 5

    elif askTimur:

        scene bg_classroom_blur with dissolve
        show jenya normala at right2 with dissolve
        show mc normala at left2 with dissolve



        j "Я попыталась заговорить с ним, но на всё получала односложные ответы. Лучше уж не говорить совсем, чем говорить так."

        j "Но, мне кажется, он этого и добивается. Хоть имя узнала - Тимур. В общем, какой-то он пугающий и мрачный…"

        n "Это же мой сосед в общаге. Ну, теперь хоть имя его знаю. Значит, он не только со мной такой необщительный."

        "Самое удивительное, что он пришёл в вуз раньше меня. И как и во все наши предыдущие встречи, всё так же спал."

        "Хоть я и не мог разглядеть лица Тимура, всё равно можно было заметить помятый вид парня."

        "Возможно, он, как и я, собирался впопыхах, но почему-то мне казалось, что он и не старался выглядеть иначе."

    elif askAlex:

        scene bg_classroom_blur with dissolve
        show jenya grina at right2 with dissolve
        show mc normala at left2 with dissolve



        j "Многоуважаемый господин староста! Очень серьёзный человек. Думаю, со своими обязанностями он точно справляется."

        j "Говоря между нами, он душноватый. Не думаю, что мы с ним сходимся."

        j "Но прозвище “Шнурок” забавное. И как же забавно он возмутился, когда я его так назвала."

        n "Шнурок сидел на первом ряду и всем своим видом давал понять, что он здесь не ради шуточек и общения. Его светлые волосы были аккуратно зачёсаны назад, а одежда была  идеально выглаженной и чистой."

        "Даже сейчас он что-то проверял в своих записях и недовольно поглядывал на болтающих парней сзади."

    elif askMargo:

        scene bg_classroom_blur with dissolve
        show jenya normala at right2 with dissolve
        show mc normala at left2 with dissolve



        j @smile "Такая забавная! Глаза сияют при виде Шнурка, а тот дурак дураком вроде умный, а ничего не понимает."

        n "И действительно, светловолосая девушка часто кидала смущённые взгляды на парня с первого ряда."

        "Но кажется его это волновало меньше всего, или он просто не замечал?"



    #Звук хлопка двери. Женя вздрагивает. Спрайт Жени грустный. Спрайт гг нейтрален

    play sound door

    "И вот наконец-то в аудитории появляется преподаватель. Он, не извинившись за своё опоздание, вальяжно направился к своему месту."

    show jenya normala at right2 with dissolve

    j "Ну вот…я уж думала, пары сегодня не будет."

    #Спрайт гг с улыбкой

    show mc smile crosseda at left2

    mc "Наверное, препод, как и я потерялся в этом корпусе."

    #Спрайт Жени с широкой улыбкой

    show jenya smilea at right2

    j "Ой, так давай я тебе после пар экскурсию проведу! Я тут всё знаю!"


    menu:

        "Согласиться":

            mc "Давай, а то я снова заблужусь, как сегодня."

            #Спрайт Жени широко улыбается с закрытыми глазами
            show jenya smilea at right2

            j @ smile "Будет весело!"

            n "С каким же светлым и улыбчивым человеком я разобщался! Я точно сделал правильный выбор. Интересно, у неё вообще бывает плохое настроение?"

            $ relate_jenya += 5

        "Не идти":
            #Спрайт смущённого гг

            $ excursion = True

            mc "Прости, сегодня не смогу"

            #Спрайт Жени с перекрещенными руками и обиженным лицом
            show jenya angrya at right2

            j normal "Ну и ладно. Если снова потеряешься, то сам виноват."

            "В памяти вслыли бесконечные лабиринты коридоров. Возможно я ещё пожалею о своём выборе."
            $ relate_jenya -= 5


    show cj_mc_jenya with dissolve
    hide jenya smilea
    hide mc normala
    $ persistent.poster1 = True

    if cookie:
        "Следующая часть пары прошла незаметно. Мы с Женей болтали и ели печенье. Как оказалось, Женя сама испекла его."

    else: #Если не согласился на печенье:
        "Следующая часть пары прошла незаметно. Мы с Женей болтали о том о сём и совсем не слушали преподавателя."

    #На фоне играет спокойная музыка
    #Фон с потоковой аудиторией

    "Сегодня я испытал невероятной степени уровень страдания. Отсидел три пары."

    "Моим первым канцлером была преподаватель английского, она была маленького роста, с забавным акцентом."

    "Существуют такие преподаватели, у которых будто бы раздвоение личности. На перемене они улыбаются тебе, смеются над твоими шутками, активно отвечают на вопросы. Но когда начинается пара, ты сразу оказываешься в ледяной пещере. Ты больше не друг, а совершенно чужой человек."

    "Возможно, это хорошо. Субординация, все дела."

    "Но всё-таки это те ещё эмоциональные качели!"

    #Возможно сделать другой фон

    "Вторая пара была с печальным и уставшим преподом. Его глаза были наполнены какой-то тоской."

    "Материал он рассказывал очень отвлечённо, будто смотрел в пустоту."

    "Множество смешков было сделано в его сторону разной степени тяжести. Каждый посчитал своим долгом что-то да сказать у него за спиной."

    "Только спустя время мы узнали, что от него ушла жена."

    "Сказать, что было неловко и стыдно - ничего не сказать."

    "Никто больше его не обзывал и не оскорблял."

    "Третья пара была с преподавательницей, которая имела в себе черты препода по английскому."

    "Но если на первой паре мы столкнулись с дилетантской сменой характера, то тут была профессиональная изобретательность."

    "Она улыбалась, шутила, кидала комплименты направо и налево во время пары."

    "Но вместе с тем, когда ей что-то не нравилось, было видно, что она может ругать с той же силой, что и хвалить."

    "Это была ювелирная работа кнута и пряника."

    "Съедобный кнут, ядовитый пряник. Наверное, это и есть верх педагогики."

    "Что касается самих пар, войти и втянуться в процесс, честно сказать, было тяжеловато. Не из-за сложности материала, а из-за противостояния весёлого окружающего мира и скучного мира знаний."

    #Смена фона на уличное окно… (В окне нарисовать солнце, но изобразить пасмурную погоду, чтобы передать атмосферу и хорошего и нагнетающего настроения. За окном достаточно изобразить берёзы, пару пролетающих птиц в небе, по-возможности дорогу с красной и синей машиной и силуэты людей. Силуэты очень простые, чтобы было понятно идёт взрослый человек или школьник, силуэты рисовать приглушенным цветом)

    scene cj_window with dissolve

    "За окном целый мир с птичками, берёзами, проезжающими машинами всех цветов радуги."
    "Школьники, несмотря на тяжесть рюкзаков, вприпрыжку бегут домой. А милые бабушки с собачками не спеша прогуливаются вдоль дороги. Только одно это целиком и полностью манило мой взгляд и мысли."


    #Музыка играет чуть более ритмично и оживленно. Мелодия приятная
    #Смена фона.Нарисовать сидящими вместе за столом гг и Женю. Цветовая палитра очень тёплая

    "Не одного меня. Женя тоже глядела в окно и часто, я так думаю, даже пыталась угадать, на что конкретно я сейчас смотрю и о чём думаю."
    "На перерывах же я открывал для себя новый мир, её внутренний мир."

    show cj_mc_jenya with dissolve

    hide cj_window

    "Послушал о том, как она случайно сожгла заброшенный дом в 14 лет, о том, какой она сейчас сериал смотрит и о том, в чём отличие хоррора от триллера."

    "Одна из одногруппниц даже вступила вместе с ней в дискуссию по этому поводу."

    #Фон сменяется на улицу с вузом на заднем плане
    #Музыка со звуками улицы

    "В конце концов, вместе мы выжили. Пожалуй, ходить на много тяжёлых пар стоит хотя бы ради чувства свободы перед открытием дверей на улицу в конце дня. Запах свободы ударяет в голову. И всё, на что ты смотрел из окна, теперь можешь потрогать руками."


    if excursion:

            #Музыка очень приглушенная
            #Смена фона на поточную аудиторию

            scene bg_classroom with dissolve

            #Спрайт Жени. Открытый рот, спокойная эмоция
            show jenya surprisea at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Ну как тебе первый день?"

            #Спрайт гг с ухмылкой на лице
            show mc smile crosseda at left2

            mc "Довольно неплохо."

            #Спрайт Жени. Открытый рот, заинтересованное лицо
            show jenya surprisea at right2 with dissolve

            j "Кстати, а где ты живёшь?"

            #Спрайт гг. Эмоция спокойная
            show mc normala at left2


            mc "В 3 общаге."

            #Спрайт Жени. Улыбающиеся лицо
            show jenya smilea at right2 with dissolve

            j "Ой, так я тоже! Пошли вместе!"

            if persistent.jenya_meet != True:
                $ renpy.notify("В дневнике появилась новая запись!")
            $ persistent.jenya_meet = True

            stop music
            play music city
            scene black with dissolve
            scene bg_street_night_winter with dissolve
            hide bg_classroom with dissolve

            "Не дожидаясь моего ответа, Женя взяла меня под руку и повела в сторону общежития."

            #Cj где гг и Женя идут в общагу

            pause 1

            scene black with off



    if excursion == False:

        scene bg_classroom with dissolve
        show jenya smilea at right2 with dissolve
        show mc normala at left2 with dissolve

        j "Ну что, готов к экскурсии от непревзойденной меня?"

        #Спрайт гг с улыбкой на лице

        show mc smile crosseda at left2

        mc "Конечно!"

        #Спрайт Жени взгляд в сторону
        show jenya normala at right2 with dissolve


        hide screen scr_over
        hide screen scr_hider


        jump ChoiceExcursion
        show jenya normala at right2 with dissolve

        label ChoiceExcursion:
            menu:
                "Столовая" if visitCanteen:
                    $ skolko_mest_na_excursion += 1
                    $ visitCanteen = False
                    jump Canteen #находится в скрипте places_excursion.rpy
                "Парк" if visitPark:
                    $ visitPark = False
                    $ skolko_mest_na_excursion += 1
                    jump Park #находится в скрипте places_excursion.rpy
                "Библиотека" if visitLibrary:
                    $ visitLibrary = False
                    $ skolko_mest_na_excursion += 1
                    jump Library #находится в скрипте places_excursion.rpy
                "По домам" if visit1 and visit2 and visit3:
                    "По домам!"


            if skolko_mest_na_excursion==3:
                #Если все три места посетили:
                #Музыка спокойная, средняя по звучанию
                #Смена фона на улицу с остановкой
                stop music
                scene black with dissolve
                pause 2
                play sound city
                play music sincerely
                scene cj_aftertalk with dissolve

                $ persistent.poster2 = True

                #Спрайт Жени. Открытый рот. Эмоция спокойная

                j "Ну, самое главное я тебе показала, можно и по домам. Ты, кстати, где живёшь?"

                #Спрайт гг. Эмоция спокойная

                mc "В 3 общаге."

                #Спрайт Жени. Улыбающиеся лицо

                j "Ой, так я тоже! Пошли вместе!"

                if persistent.jenya_meet != True:
                    $ renpy.notify("В дневнике появилась новая запись!")
                $ persistent.jenya_meet = True

                "Не дожидаясь моего ответа, Женя взяла меня под руку и повела в сторону общежития."

                pause 1

                scene black with dissolve


    #Сон с Евой
    #Чёрный экран с анимацией падающего снега, на фоне звуки ветра.
    #Появляется диалоговое окно от неизвестного. Текст белого цвета.
    play music city
    pause 2
    show snow1
    show snow2
    with dissolve

    un "Снова ты?"

    "Из темноты раздался уже знакомый голос. Казалось, что со мной говорила сама темнота."

    mc "Снова я. Я не знаю, как сюда попал."

    #Спрайт черный силуэт человека

    "За пеленой снегопада я разглядел приближающийся силуэт. Теперь я был точно уверен, что мой собеседник - девушка, но её очертаний лица мне было не разглядеть."

    "Я будто оказался в мире двойственностей. Мне было хорошо и легко, но в то же время тревожно и непонятно."

    "Мне было всё интересно, но и абсолютно всё равно."

    "Я был свободен, свободнее любой птицы в небе, но в то же время я был прикован к земле, к деревьям вокруг, к девушке, стоящей передо мной."

    "Мы с ней, казалось, были на одной волне, и это меня успокаивало и  пугало одновременно, невероятно пугало. Она, наконец, уничтожила тишину задумчивым…."

    un "Наверное, в парке сейчас так красиво…"

    #Если ходил на экскурсию:
    #Спрайт гг. Смущенное лицо

    if visitPark != True:

        mc "Да, там очень красиво."

    else:   #Если не ходил на экскурсию:

        mc "Я там ещё не был."

        #Спрайт гг. Грустное лицо

        un "Тебе стоит туда сходить."

        #Спрайт черного силуэта

    "Между нами повисла холодная тишина, лишь ветер осмеливался её нарушить."

    "Возможно, если прислушаться, можно было услышать сообщение, что он пытался передать."

    un "Жаль, я не увидела как цветут яблони в парке."

    "Голос незнакомки всегда звучал неожиданно и резко. Словно холодная горсть снега, что внезапно попала за шиворот."

    #Спрайт гг. Заинтересованное лицо


    mc "Что…что ты имеешь ввиду?"

    #Спрайт черного силуэта

    un "Я…"

    #Звук сирены скорой помощи

    play sound ambulance

    "Звук её ответа был будто проигран задом наперёд."

    "Но что удивительно, я почти догадался, что она имеет в виду. Возможно, я бы понял, что она ответила, если бы не громкий звук сирены в моей голове."

    "Голову словно кто-то сжимал."

    "Я надавил на свои виски, и вся двойственность кончилась."

    "Осталась только боль, жгучая, как удар скорпиона, и продолжительная, как свежее клеймо."
    "Я не слышал больше ничего, кроме этой сирены, постепенно погружаясь во тьму. И, чем темнее становилось вокруг, тем тише был звук сирены."

    "И вот, когда я, казалось, достиг дна этой темноты, я проснулся, и цвет, что я видел, сменился на белый, цвет потолка моей комнаты в общаге."

    stop sound
    stop music
    scene black with off

    pause 1

    scene bg_room_morning_blur with onn

    hide snow1
    hide snow2

    #Фон комната в общаги.

    "Голова чуть болела, но в целом я чувствовал себя как обычно."

    scene bg_room_morning at pan
    with dissolve

    play music room

    "С трудом повернувшись, я выглянул в окно, на дорогу за общагой."

    #Вид на улицу (видно дорогу)

    scene cj_room_window with dissolve

    play sound ambulance2

    "Уборщик подметал мусор, мужчина в костюме шёл по своим, наверняка очень важным делам, а за поворотом исчезала из виду машина скорой помощи, с тем же звуком, что только что, казалось бы, разрывал мою голову на несколько частей."

    "Это был всего лишь сон. Жизнь идёт своим чередом. Я выдохнул и попытался поспать ещё раз, но, хоть убей, больше не хотелось."
    if persistent.jenya_dreamcontinue != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.jenya_dreamcontinue = True

    #Фон комната гг

    "Забросив идею со сном, я решил хоть немного взбодриться и направился в умывальную."

    "Это решение показалось мне разумным, потому что во время школы этот метод всегда помогал мне растрястись и настроиться на нужный лад."

    play sound steps
    stop music
    scene black with dissolve
    scene cj_nocockroach with dissolve

    play music shower

    #В ванной (возможно пол в душевой или стена, но там где внезапно появится таракан).
    #Звук шума воды в душе.

    "Я позволил себе расслабиться, пытаясь смыть с себя все негативные мысли и страхи, которые преследовали меня после странного сна."

    "Я не понимал, к чему мне это снится, но умывание действительно давало успокаивающий эффект."

    "Постепенно я начал чувствовать, как напряжение покидало моё тело, и спокойствие возвращалось ко мне. Я закрыл глаза и постарался сосредоточиться только на звуке воды, который успокаивал мои нервы."

    "Теперь я был готов начать свой новый день без страха и тревог."

    #Скример таракана

    scene cj_cockroach_screamer1 at zoomin

    play sound screamer

    pause 1

    scene cj_cockroach_screamer2 at tremble

    pause 1

    "Какие же неожиданные гады! Какая мерзость! Неужели я когда-то смогу к этому привыкнуть?"

    scene cj_nocockroach with dissolve

    "И куда скрылся этот таракашка?"

    "Ой, фу, неважно. Надеюсь он убежал и больше мы с ним не пересечемся."

    stop music
    play sound steps
    scene black with dissolve
    scene bg_room_morning with dissolve
    play music room

    "После я вернулся в комнату."

    "Она вызывала у меня чувство комфорта, и я ощущал даже некий уют. Отсутствие учебных задач и откровенная лень поставили меня перед вечным выбором: чем же теперь заняться?..."

    menu:

        "Пойти на кухню":

            mc "Блин, я же ещё не ел…надо что-то сварганить. Жаль, что я не слушался маму, когда она пыталась научить меня готовить."

            "Благо моя комната недалеко от кухни. "

            scene black with dissolve
            scene bg_hallway_light with dissolve

            "Я прошёл через коридор общаги, уже ставший мне привычным."

            scene bg_kitchen_evening with dissolve
            play music evening

            "Вошёл в место, где будут готовиться мои “кулинарные шедевры”."

            "Кухня была оснащена несколькими электроплитами, микроволновками, мойками для посуды и общими холодильниками."

            "Я взял свои продукты и подошёл к плите, в надежде, что не испорчу еду, которую трудно было испортить."

            "У плиты стояла моя новая знакомая - Женя. От запаха еды у меня ещё больше разыгрался аппетит."

            show mc normal homea at left2 with dissolve

            mc "О, доброе утро."

            show jenya normal homea at right2 with dissolve

            j "Что-то ты неважно выглядишь, у тебя всё хорошо?"

            mc "Да не, всё нормально."

            n "Я решил, что пельменей будет достаточно для начала дня."

            "Открыв упаковку пельменей, я хотел было приступить к “чуду кулинарии”, но..."

            j "Ты действительно будешь это есть!?"

            #У Жени в шоке распахиваyтся глаза

            j "Сейчас же только утро, а ты пельмени есть собрался…"

            mc "Ну… ничего нормального всё равно нет, так что придётся есть это."

            n "Не понимаю, чем это было вызвано, но выражение лица Жени резко сменилось. Оно приняло недоуменный и слегка осуждающий вид. Немного подумав, она подуспокоилась и спокойно спросила…"

            j "Слушай, а какой у тебя номер комнаты?"

            mc "Ну 205, а тебе зачем?"

            mc "В гости хочешь заглянуть?"

            j "Да так…"

            mc "Ну ты это, заходи, если что. Всё равно с соседом нормально не поболтать."

            j "Возьму на заметку"

            #Съедает завтрак и перекинувшись ещё несколькими фразами с Женей, возвращается в комнату

            n "К этому моменту мой завтрак был готов."

            "Однако блюдо определённо получилось съедобным. Это меня порадовало, и я принялся уплетать свой “недозавтрак”, по мнению Жени."

            "Женя села рядом. Мы обсудили нашу учебу, поговорили о том, какой я безнадёжный повар и о гирляндах, которыми Женя собралась завесить свою комнату."

            $ relate_jenya += 5
            $ eda = True

        "Разобрать вещи":

            play music sincerely

            "Пора бы уже разобрать вещи из своего чемодана."

            "Я начал тихо раскладывать свои вещи, стараясь не шуметь, чтобы не мешать соседу, который до сих пор спал. Однако мои усилия, казалось, были напрасными, потому что из-за моих шевелений вещами шума было не избежать."

            show timur angry with dissolve

            t "Эй, ну ты можешь не шуметь с утра пораньше?!"

            "Мне было искренне стыдно перед ним. Нет ничего хуже чем когда тебя будят ранним утром. Тем более, по сути, абсолютный незнакомец."

            hide timur angry with dissolve

            "В целом, я уже знаю дальнейшее развитие событий. Варианта всего два:.."

            "В первом варианте, мы становимся закадычными друзьями и живем будто братья. Второй вариант: Мы остаёмся пассивными знакомыми."

            "Кажется, мои шумы были критическими - больше он не сомкнул глаз. Достал свои чёрные беспроводные наушники и стал что-то смотреть."

            "Краем глаза я заметил у него в телефоне фотографию Теда Банди. Видимо, он любит тру крайм. В худшем случае Теда Банди. Прям в очень худшем случае."

            "Может, почитать википедию про какого-нибудь маньяка и попытаться найти с ним общий язык? Дожили. Хочу почитать про серийные убийства ради того, чтобы пообщаться с соседом по комнате."

            "За всё время моего пребывания здесь, мы толком и не поговорили. Сказали друг другу всякие мелочи и всё."

            "С ним разговаривать, это как будто собственными руками вытаскивать из воды якорь. Ну, если якорь, конечно, состоит из пассивной агрессии, меланхоличной тяги к одиночеству и желанию выбить из меня все миллиард мыслей о том, как с ним заговорить."

            "А может, мне только так кажется, и он как шалтай-болтай. Бледный снаружи, золотой внутри."

            "Однако, это долго продолжаться не может. Я не хочу быть просто знакомым. Мне нужно попробовать сломать лёд между нами любой ценой."

            "Может, мне стоит попробовать с ним поговорить? Как никак нам ещё долго предстоит жить вместе."

            menu:
                "Поговорить":

                    show mc normal homea at left2 with dissolve
                    mc "Давай нормально познакомимся? Нам всё-таки с тобой несколько лет жить вместе. Откуда ты?"

                    show timur normala at right2 with dissolve

                    t "..."

                    n "Он просто игнорирует меня. Даже не мычит. Он полностью окунулся в яркий мир какого-то аниме, что смотрел в своём телефоне."

                    "Я попытался ещё пару раз неловко что-то сказать. Даже с агрессией. Ничего не помогало. Я даже попытался узнать, что за аниме он смотрит, но он повернул экран так, чтобы я ничего не видел."

                    show mc normal homea at left2 with dissolve

                    "Уверен, он сейчас хочет быть как Робинзон Крузо. Один на острове. И я этого хочу."

                    "Возможно, что даже волейбольный мяч был бы лучшей компанией, чем мой сосед."

                    mc "Вот и поговорили."

                "Не разговаривать":

                    "Он снова не настроен на разговоры…"


    if eda:

        pause 2

        scene black with dissolve

        play sound stuk

        #Стук в дверь.
        "Кто это мог бы быть?"

        scene bg_room_evening at pan
        with dissolve

        "Может, комендант? Ладно, выбора нет."

        #Звук открывания двери

        play sound door

        "За дверью никого не оказалось, но на полу лежала тарелка, обёрнутая в пищевую плёнку."

        "В тарелке был свежий завтрак."

        "Запах омлета с сыром и помидорами заполнял комнату. Кажется, даже Тимур оживился и поглядывал на меня."

        "Только один человек мог сделать для меня такой сюрприз - Женя."

        "Я почувствовал тепло и любовь от этого жеста и с удовольствием принялся за второй завтрак."

        if persistent.jenya_endchap1 != True:
            $ renpy.notify("В дневнике появилась новая запись!")
        $ persistent.jenya_endchap1 = True

        "В этот момент я понял, что познакомиться с Женей было самым верным решением."


    scene black with dissolve

    stop music


    #return

    jump jenya_cp2
