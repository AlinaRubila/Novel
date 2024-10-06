# Начало рута Тимура
define talkWith = False
define seeJenya = False
define seeAlex = False
define seeTimur = False
define seeMargo = False
define visitKitchen = True
define visitDayroom = True
define visitLaundry = True
define dormPlaces = 0
screen guySee():
    imagebutton:
        xalign 0.5189
        yalign 0.411
        auto "images/rutChoice/jenya_button_%s.png" focus_mask True action [SetVariable("seeJenya", True), Return(value=None)]
    imagebutton:
        xalign 0.7889
        yalign 0.825
        auto "images/rutChoice/alex_button_%s.png" focus_mask True action [SetVariable("seeAlex", True), Return(value=None)]
    imagebutton:
        xalign 0.914
        yalign 0.563
        auto "images/rutChoice/timur_button_%s.png" focus_mask True action [SetVariable("seeTimur", True), Return(value=None)]
    imagebutton:
        xalign 0.0895
        yalign 0.357
        auto "images/rutChoice/margo_button_%s.png" focus_mask True action [SetVariable("seeMargo", True), Return(value=None)]
label timur:

    if persistent.ending1 and persistent.ending122:
         scene bg_rut
    else:
        scene bg_rutnoeve

    "Думаю совместная учеба будет хорошим поводом мне познакомиться и стать ближе со своим соседом по комнате. Сяду к нему."

    "Однако как-то странно, что он пришел сюда раньше меня. Идти нам одно и то же расстояние и одним и тем же путем, но он уже здесь, а я только пришел. Пусть это будет одной из множества его загадок."

    #Спрайт Гг улыбается.
    mc "Привет. Можно сесть?"

    #Спрайт Тимура обычный.
    un "..."

    "Не дождавшись ответа, я сел рядом."

    mc "Какой-то совсем не разговорчивый… Может, не выспался?"

    "Мой потенциальный друг лишь поднял глаза вверх и тотчас же опустил их вновь, так ничего мне и не ответив."

    "Молчание – знак согласия, так что я кинул свои вещи рядом с ним и присел. Вещи, брошенные мною, сформировали определенную стену между нами, будто бы эмоциональной стены было недостаточно."

    "Было скучно."

    "Я смотрел вокруг, изучал лица окружающих меня людей и внезапно понял, что не знаю никого из них по имени. Даже человека, сидящего рядом со мной, хотя я с ним теперь живу."

    "Как можно не знать имени человека с которым живешь? Разве это не странно?"

    "По сути, этот человек может сделать с тобой всё что угодно, пока ты спишь или гуляешь, к примеру."

    "Наверное, мне стоит уважать его нежелание общаться. Всё-таки он очень явно это показывает."

    "Возможно, лучший способ наладить контакт с молчаливым человеком – это молчать вместе. И к тому же учитывая его грозный вид, это будет наиболее безопасным вариантом."

    menu:
        "Заговорить":
            mc "Привет, меня зовут [mcname], а тебя?"
            $ talkWith = True

            "Что ж, попытка наладить отношения не увенчалась успехом. Он абсолютно не расположен со мной общаться."

            "Ни слова в ответ, а в качестве добивающей атаки он и вовсе повернул голову к окну, рассматривая небо. Но сдаваться рано, попробую зайти через стратегию сожительства."

            #Спрайт Гг обычный.
            mc "Мы с тобой теперь живем в одной комнате. Надеюсь поладим, как никак несколько лет вместе жить. Ты не волнуйся, я не слишком конфликтный."

            "Ни слова в ответ. Это тотальный разгром по социальным фронтам."

            "Один кивок с его стороны - всё, чего я смог добиться."

            "Похоже, что я умудрился настолько наскучить ему, что сразу после окончания моего монолога он лёг на парту, используя свои руки в качестве подушек, и не поднимал голову."

            "Продолжать уже смысла нет, разве что для того, чтобы его позлить, но зачем мне это? Ну и недружелюбный парень."

            "Повезло мне с соседом, ничего не скажешь. И что самое худшее, с соседом не только на пару, а еще и на комнату. Ну и удача. А ведь впереди меня сидят две девушки, которые всю пару о чём-то шепчутся. Ведут диалог. Честно сказать, даже завидую."

            "От нечего делать я решил ещё раз посмотреть на одногруппников, более внимательно."

            "Не более 50 процентов информации о человеке можно выяснить, опираясь только на его слова о себе и окружающих. Остальное складывается из мимики лица, жестов рук, непроизвольных взглядов, и прочих, будто бы неважных деталей. Надеюсь, узнаю их получше, если хорошенько взгляну."

        "Молчать":
            "Пожалуй, мне лучше уважать его нежелание со мной говорить."

            "Вместо того, чтобы пытаться вытянуть из человека, который не желает с тобой общаться, какую-то информацию, предпочту хорошенько рассмотреть своих одногруппников."

            "Тем более, что мой сосед уже лёг на парту, чтобы вздремнуть, что лишь доказывает, что он вообще не хочет разговаривать."

            "Его дело. Я, конечно, ошибся с выбором. Лучше бы сел к кому-нибудь другому, может  завязался бы настоящий диалог."

            "Но придется довольствоваться тем, что есть и просто попытаться хотя бы что-то выяснить о своих одногруппниках, взглянув на них."

    call screen guySee
    if seeJenya:
        "Рядом с нами сидела рыжеволосая девочка. С виду она очень даже милая. Интересно, что она пишет в своём блокноте? Или она рисует? Выглядит она очень стильно, похожа на творческого человека. Интересно, почему она выбрала направление информационной безопасности?"
    if seeAlex:
        "На первом ряду сидел светловолосый парень. Одет он очень официально. Видно, опрятный и ухоженный. Взгляд очень серьезный и сосредоточенный."

        "Хоть преподаватель еще и не пришёл, мальчик уже открыл тетрадь и задумчиво держал ручку в руках. Мне кажется, он сможет стать старостой, выглядит очень ответственным человеком."
    if seeMargo:
        "Мой взгляд остановился на светловолосой девочке. Судя по всему, семинары и лекции – далеко не самая важная для неё вещь в этой аудитории."

        "Я заметил, что она слишком часто поглядывает на парня с первого ряда. И каждый раз вздыхает. Она точно где-то в своих мыслях. В мыслях об их будущем? Интересные одногруппники, мне кажется у них бы могло что-то получиться. Хотя откуда мне знать?"
    if seeTimur:
        "Мой сосед по парте оставался неизменным. Он лег на парту и надел наушники. Очевидно, что пара его абсолютно не интересует. Да и знакомиться со мной он желанием не горит… Это уж точно."

    if talkWith:
        "Видимо меня ждут годы одиночества при наличии соседа по комнате. Это хуже всего. Я как бы с ним, но в то же время и нет. Неужели он не понимает, как важен налаженный контакт между людьми? Почитай книжку о том как улыбаться, Влад Дракула."
    else:
        "Он явно не самый болтливый человек на свете, но возможно у него просто сейчас нет настроения."

        "Может быть, случилось что. Завтра будет новый день, и, может быть, лучи восходящего солнца сумеют зарядить его позитивом."

    "Остаток дня был преступно скучен, время шло медленнее, чем улитка, ползущая в замедленной съёмке. Иногда я от скуки просился в туалет, а сам в это время просто ходил и смотрел вокруг или сидел в телефоне."

    "Делал я это настолько часто, что наверняка у всех сложилось впечатление, что у меня проблемы с мочевым пузырем или c желудком."

    "Пусть так, это лучше, чем сидеть в этой тюремной камере вечность. Но, стоит сказать, что в конце дня произошел приятный сюрприз – одну из пар отменили, не знаю почему."

    "Ходят слухи, что тот препод, у которого отменили пару, в принципе очень проблемный и может не явится на пару только лишь по своему желанию. Однако, большинство студентов этому только рады."

    #Фон крыльца третьей общаги
    #Музыка энергичная.

    "Когда я подходил к общаге, увидел невысокую милую женщину."

    "Она стояла, прислонившись к стене."

    #Спрайт Гг удивлённый.
    mc "О, Здравствуйте."

    #Спрайт ОД с улыбкой.
    un "Здравствуй, ты из какой комнаты?"

    #Спрайт Гг обычный
    mc "Я из 412."

    #Спрайт ОД.
    un "О, так ты в комнате с Тимуром?"

    mc "Кажется да, правда я ещё не знаю его имени, он всё время молчит."

    un "Тогда это точно Тимур, ты не переживай, он хороший человек, просто закрытым стал. Я, кстати Ольга Дмитриевна – комендант общежития."

    mc "Я [mcname], приятно познакомиться."

    od "Хочешь проведу небольшую экскурсию?"

    #Спрайт Гг, улыбается.
    mc "Было бы неплохо."

    od "Что первым хочешь посмотреть?"
    jump ChoiceDorm

    label ChoiceDorm:
        if dormPlaces < 3:
            menu:
                "Кухня" if visitKitchen:
                    $ dormPlaces += 1
                    $ visitKitchen = False
                    jump Kitchen
                "Комната отдыха" if visitDayroom:
                    $ dormPlaces += 1
                    $ visitDayroom = False
                    jump Dayroom
                "Прачечная" if visitLaundry:
                    $ dormPlaces += 1
                    $ visitLaundry = False
                    jump Laundry
    #Спрайт ОД.
    od "Ну вот, вроде бы всё показала, но если вдруг возникнут вопросы, то обязательно приходи."

    #Спрайт Гг улыбается.
    mc "Спасибо вам большое."

    od "А также есть несколько правил."
    od "Не пить, не курить, не мусорить."
    od "Убираться в комнате самим, бережно к ней относится."
    od "Не шуметь после 23:00."
    od "Возвращаться в общежитие до 00:00."

    #Спрайт Гг обычный.
    mc "Хорошо, я понял."

    "После небольшой экскурсии от коменданта, я вернулся в комнату. Я рад, что Ольга Дмитриевна показала мне общагу, теперь хоть понимаю, где живу."

    "Этот день сильно меня вымотал. Я понимал, что первый учебный день будет тяжелым, но не думал, что настолько…"

    "Я быстро переоделся в домашнюю одежду."

    "Общажная кровать, в удобстве которой я сомневался, сегодня показалась мне на удивление мягкой. Я провалился в сон в тот же миг, как моё лицо коснулось подушки."

    #Фон чёрного экрана с падающим снегом.
    #Звуки метели.
    "Сквозь сильную метель пробивался женский силуэт. Я узнал его, именно с ним мы разговаривали в прошлый раз."

    #Спрайт чёрного женского силуэта Евы.
    un "Вот мы и снова встретились."

    "Моя тайная преследовательница улыбалась. Её лица не было видно из-за пелены снега. Но я знаю, что она улыбается, я это чувствую."

    "Меня передёрнуло от страха. Я был полон непонимания, этот силуэт сводил меня с ума. Проглотив ком в горле, я прокричал:"

    #Спрайт Гг злой.
    mc "Кто ты? Почему ты мне снишься? Что ты хочешь от меня?!"

    #Спрайт чёрного силуэта Евы.
    un "Найди меня."

    "Что? Что всё это значит? Но этот вопрос я задал уже в пустоту. Силуэт стал размытым, а затем и вовсе слился с белой пеленой метели."

    "Всё медленно прояснилось и посветлело. Девушка исчезла, а я оказался в каком-то помещении. Что происходит?"

    "Находясь в полном недоумении, я пытался понять, реально ли всё вокруг меня."

    #На фоне плавно начинает играть спокойная музыка.
    #Медленный переход (можно сделать переход с морганием Гг) на общажную комнату.

    "Я пробежался взглядом по помещению. Перекошенный карниз, мой чемодан, вещи, которые я вчера не разобрал из-за усталости. Напротив меня спал мой новый товарищ – Тимур. Я определённо в своей комнате."

    "Что это было? Почему я опять увидел эту девушку? Почему она сказала ее найти? У меня было очень много вопросов и ни единого ответа."

    "Чтобы разогнать эти мысли и окончательно прийти в себя, я направился в душ."

    #Звук шума воды в душе.
    #Фон душевой комнатки.

    "Вода окутывала меня теплом и успокаивающим шумом. Я позволил себе расслабиться под тёплыми струями, пытаясь смыть с себя все негативные мысли и страхи, которые преследовали меня после странного сна. Я не понимал, к чему мне это снится, но принятие душа действительно давало успокаивающий эффект."

    "Постепенно я начал чувствовать, как напряжение покидало моё тело, и спокойствие возвращалось ко мне. Я закрыл глаза и постарался сосредоточиться только на звуке воды, который успокаивал мои нервы."

    #Фон комнаты Гг.

    "В душе я был примерно полчаса, но когда я вернулся, ничего не изменилось. Тимур спал все в той же позе."

    "Я уселся на стул и стал думать, чем заняться, обводя комнату глазами."

    "Моё внимание привлёк большой чемодан, стоящий возле шкафа, который надо было наконец разобрать."

    "Я стал медленно расстегивать молнию, открывая чемодан, стараясь быть как можно более тихим, но в тишине комнаты, жужжание собачки молнии было похоже на рёв мотора гоночного болида."

    "Как назло, в чемодане лежало чертовски много пакетов, каждое прикосновение  к которым безжалостно разрывало тишину комнаты."

    "С опаской я поглядывал на соседа, который лежал на боку, отвернувшись от меня. То и дело мне казалось, что я слышу звуки с его стороны."

    "Повернувшись обратно, я увидел, что он уже развернулся и сверлил меня злобным взглядом человека, чей сон так нагло прервали. Видимо, стоит заканчивать с раскладыванием вещей, по крайней мере, пока Тимур не проснется."

    #Перед скримером должна быть тишина, а после звук пробегания насекомого.
    #Скример таракана.

    #Спрайт испуганного Гг.
    mc "Твою ж…!"

    #Спрайт злой Тимур.
    t "Ты что орешь с утра пораньше?! Спать мешаешь. В единственный выходной!"

    #Спрайт испуганного Гг.
    mc "Да у нас в комнате..."

    "Я опять обернулся на своего соседа, но его уже не волновал ни я, ни этот огромный таракан. Тимур просто скрылся под одеялом."

    "Таракан к тому времени, кстати, тоже убежал в неизвестном направлении. Все вернулось на круги своя."

    "Ну и денёк… С самого утра всё идёт не так. Этот сон, таракан, да и Тимур совсем не хочет дружить."

    "Да не то что дружить, он даже всерьез меня не воспринимает. Он какой то слишком злой и грубый. Непонятно, что с этим делать, да и желание что-то менять уже пропадает."

    "Пойду-ка проветрюсь. Надо сходить в магазин, а то есть совсем нечего. Заодно выпущу пар."

    "Я оделся потеплее, взял рюкзак и собрался выходить. Уже было собрался выйти, но тут во мне что-то щелкнуло."

    "Я посмотрел на своего соседа, он лежал на кровати со своим неизменным угрюмым выражением лица. Мне стало немного стыдно за то, что я с самого утра был таким шумным."

    menu:
        "Спросить":
            #Спрайт Гг обычный.
            mc "Тебе что-то взять в магазине?"

            #Спрайт злой Тимур.
            t "Да вали ты уже."

            "Что ж, ничего нового. Другой реакции я и не ожидал… Сделал вид, что грубость Тимура никак меня не задела. Тем не менее из общежития я вышел с испорченным настроением."
        "Не спрашивать":
            "Я замер у двери, Тимур в очередной раз с осуждением посмотрел на меня. Этот взгляд убил моё желание как-либо ему помогать. Я решил пойти в магазин и купить лишь нужные мне товары. Тимур и сам справится, обойдется!"

    #Фон улицы.
    #Активная мелодия.
    "Я вышел из общежития. Морозный ветер ударил мне в лицо."

    "По пути в магазин, в голове я прокручивал события этого утра. Сначала я и правда корил себя за то, что шумел, пока сосед пытался поспать."

    "Но постепенно чувство стыда переросло в агрессию. Не так уж и громко я разбирал чемодан, да и это не мои проблемы, что он в 12 часов дня ещё не встал с кровати!"

    "Это не даёт ему права так грубить мне. И вообще почему только я делаю какие-то шаги навстречу. Он тоже должен понимать, что нам вместе жить еще целых 4 года. А он всё грубит и грубит."

    "Всё, с меня хватит. Не хочу больше общаться с Тимуром! Только если по делу, или в крайних случаях. Лучше с кем-то другим из группы сдружусь."

    "События утра прокручивались в моей голове снова и снова. Я вспомнил о сне. Силуэт и голос моей таинственной незнакомки не давали покоя. Я не знаю, что делать с этими снами. Она сказала найти её… Что это всё значит?"

    "Мои мысли прервал супермаркет, оказавшийся прямо передо мной. Витая в облаках, я даже не заметил, как дошёл до него. Я зашёл внутрь."

    #Фон внутри пятёрочки.
    #Спокойная музыка на фоне, с приглушёнными звуками пробивания продуктов.
    "Я ходил по торговым прилавкам, и постепенно моя корзина наполнялась продуктами."

    "Ничего особенного – всё то, что едят студенты."

    "Я набирал продукты механически и не глядя, как вдруг моё внимание привлёк стеллаж с журналами. На нижней полке я увидел яркую обложку со знакомым персонажем."

    "Я присел на корточки и взял журнал в руки. Не может быть. С яркой обложки на меня смотрела главная героиня моего любимого аниме “Маленькая волшебница и её магические друзья”. Вот это удача!"

    "Никогда не видел, чтобы такие журналы продавались прямо в супермаркете. Этот ещё и последним остался!"

    "Я пролистнул журнал и увидел крутой постер с моим любимым персонажем. Не думая больше ни секунды, я положил журнал в корзину и направился на кассу."

    "По пути к общаге я уже не думал о неудачном утре. Я представлял, как круто будет повесить свой новый постер из журнала на стену. Этот элемент интерьера станет для меня поддержкой, и хоть что-то в нашей с Тимуром комнате будет вызывать позитив."

    "С нетерпением я пришел в общежитие. Быстро убрав продукты в холодильник, я, полный счастья, отправился в свою комнату."

    #Фон комнаты Гг.
    "Когда я вошёл, мой сосед уже не спал. Он сидел на кровати и переписывался с кем-то. На то, что я вошёл в комнату, он не обратил внимания. Ну и пусть, хотя бы без негатива в этот раз..."

    "Я быстро скинул верхнюю одежду, сел на кровать и начал разглядывать журнал. Я нашел страницу с постером. Аккуратно, чтобы не повредить его, я вырвал постер из журнала."

    "Вооружившись скотчем, я принялся примерять постер на стену. Над кроватью он выглядел как-то странно, у выхода тоже. А вот над столом смотрелось в самый раз!"

    "Я аккуратно прилепил постер на стену, много раз перепроверил, чтобы всё смотрелось ровно."

    #Фон такой же, НО с добавлением плаката на стену!
    "Идеально."

    "Я отошёл немного подальше от стены. Выглядит чудесно! Этот постер не мог не вызывать у меня улыбку, как хорошо, что я его нашёл. Но тут внезапно из-за спины я услышал угрюмый голос…"

    #Спрайт злой Тимур.
    t "Сними постер."

    #Спрайт злой Гг.
    mc "Не буду, почему я должен его снимать?"

    t "Потому что я не хочу, чтобы это здесь висело!"

    mc "Да не буду я ничего снимать из-за твоей хотелки!"

    "Он поднялся с кровати и стал двигаться в мою сторону, прожигая меня взглядом."

    "Если бы мы были персонажами мультфильма, из его ноздрей бы шёл дым."

    "Его фигура всё увеличивалась и увеличивалась, пока он не приблизился настолько,что я стал дышать ему в грудь."

    "Он смотрел на меня сверху вниз так, что все его вздувшиеся вены были как на ладони. Сквозь зубы он процедил:"

    #Спрайт злой Тимур.
    t "В последний раз говорю, сними постер. Cейчас же."

    #Спрайт злой Гг.
    mc "Нет!"

    "Кажется, ему было всё равно на мои слова. Иначе как объяснить тот факт, что сразу после моего категоричного отказа он рывком протянул руку с целью сорвать плакат?"

    "Я не понимаю, кем он себя возомнил, что может решать что мне делать в нашей комнате!"

    "Резким движением я оттолкнул его руку и сделал маленький шаг вперёд, чтобы оказать на него хоть какое-то давление. Из-за разницы в росте, к сожалению, особого эффекта я не добился, но зато угрозу в виде его руки убрать удалось."

    mc "Эй, а ну руки убрал!"

    "Тимур в ярости взял меня за плечи, поднял, и аккуратно, не смотря на всю свою ненависть, поставил сбоку."

    "Тут же воспользовавшись моим изумлением, этот дылда сделал шаг вперёд и схватился за угол плаката начав его срывать, другой рукой держа меня за лоб, словно ребёнка, чтобы я не приближался."

    "Оскорблённый и разозлённый я оттолкнул его руку от своего лица и со всей силы схватил другую руку, протянутую к плакату."

    "Со всей силы я дернул её вниз, но вышло так, что пальцы Тимура не отпустили плакат во время моей атаки, и вместе с плакатом он случайно вырвал и огромный кусок обоев, который по случайному стечению обстоятельств задел карниз со шторами."

    #Тяжёлый звук падения карниза.
    #Фон комнаты Гг, но теперь разрушенной.
    "Карниз рухнул нам с Тимуром на головы, оставив нам шишки на макушке и заодно охладив головы."

    "Мы с моим противником, смотря на весь беспорядок, произошедший из-за этого инцидента, решили устроить небольшое перемирие."

    "Когда наши с ним глаза пересеклись, на наших с ним лицах отчетливо читался ряд одинаковых мыслей:"

    "Ты виноват.
    Я тебя ненавижу.
    Ты худший сосед на свете."

    "Ну, хоть в чём-то мы мыслим похоже."

    "Как назло неприятные совпадения не закончились. Дверь была не заперта, а значит, любой мог войти в нашу комнату в этот момент, когда у нас на полу валяется карниз от штор, порванный плакат, а наши обои будто бы встретились с толпой обезумевших кошек."

    "Например, могла войти Ольга Дмитриевна. Конечно же, если что-то может пойти не так, именно так оно и идёт."

    #Спрайт Од.
    od "Что у вас тут…"

    "Она даже не смогла договорить. Видимо такой беспорядок на её практике случался нечасто. Со стороны возможно действительно можно решить, что мы сделали это специально. Она смотрела на всё ошарашенными глазами, и как назло со стены продолжал медленно сползать кусок обоев."

    #спрайт коменды должен быть недовольным!
    od "Что это такое? Что вы тут устроили? Как это понимать?!"

    #Спрайт злой Гг.
    mc "Это он во всём виноват!"

    #Спрайт злой Тимур.
    t "Это я виноват?! Да если бы ты послушал меня, ничего бы этого не было!"

    od "Значит так, если вы не хотите столкнуться с дисциплинарным взысканием, то вам придётся сделать ремонт."

    mc "Но..."

    od "Я всё сказала."

    "Я было хотел что-то сказать, но она, переняв агрессивное настроение нашей комнаты, развернулась и ушла, хлопнув дверью, окончательно тем самым добив едва державшийся кусок обоев, заставив его принять поражение и рухнуть."

    "Тимур словно дикий зверь что-то рычал и бубнил себе под нос, пока шёл обратно в свою берлогу, явно желая спрятаться на кровати от меня, проблем, и всего мира."

    "А ещё, от этого плаката, разорванного пополам. Что-то в нем сильно разозлило Тимура. Но прямо сейчас, если честно, мне даже не хотелось об этом думать."

    "Единственная мысль, что была сейчас у меня в голове, была о Тимуре. Суть её была довольно проста: ну и урод."

return
