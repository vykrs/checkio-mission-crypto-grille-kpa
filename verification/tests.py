"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    'Basic': [
        {
            'input': ['quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz',
                      'quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves'],
            'answer': ['XXXX....',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....',
                       '........',
                       '........',
                       '........',
                       '........']
        },
        {
            'input': ['willbondyieldgoupordownorremainthesameifyoureatvpunditandyourjob',
                      'pwuiplolbnodnrddiytioewldagnonuodhyersramoeuiefmryjoauireoabtnvt'],
            'answer': ['.X.X.X.X',
                       'X.X.X.X.',
                       '.X.X.X.X',
                       'X.X.X.X.',
                       '........',
                       '........',
                       '........',
                       '........']
        },
        {
            'input': ['rotatingcardangrilleisatypeoftranspositioncipherthetextiswritten',
                      'rotatinithetexgltnspoiclsseiiwasrtaritdttiyangrpeoeoftranncipher'],
            'answer': ['XXXXXXX.',
                       '......X.',
                       '......X.',
                       '......X.',
                       '...X..X.',
                       '...XXXX.',
                       '........',
                       '........']
        },
        {
            'input': ['pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx',
                      'pythndoieransgnbiveofesraryifossfevtstuffreandarxirdyextxnelgawi'],
            'answer': ['XXXX..X.',
                       '......X.',
                       '......X.',
                       '......X.',
                       '...X....',
                       '...XXXXX',
                       '...X....',
                       '...X....']
        },
        {
            'input': ['weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong',
                      'wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz'],
            'answer': ['X...X...',
                       '.X.....X',
                       '..X...X.',
                       '...X.X..',
                       'X.....X.',
                       '...X...X',
                       '..X.X...',
                       '.X...X..']
        },
        {
            'input': ['youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat',
                      'ytezoieruoozsnomyuhadkolbiuiesltdyowrfskeritaosgysdmraeareliatit'],
            'answer': ['X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.']
        },
        {
            'input': ['eikqyorzsaoufwexsseeroqdukftdfkatdtrdpekefkyjaekjkuyswkorzddkpxp',
                      'eijktdsskquytreerodpswyoqdekkorzefuksarzkyftouddkpfwdfjaxpexkaek'],
            'answer': ['XX......',
                       'XX......',
                       '......XX',
                       '......XX',
                       '....XX..',
                       '....XX..',
                       '..XX....',
                       '..XX....']
        }
    ],
    'Extra': [
        {
            'input': ['ifatreefallsinaforestandnoonehearsitdoesitmakeasoundonemaysayyes',
                      'oresrsittanddoesnoonitmaeheakeasifatoundreefonemallsaysainafyyes'],
            'answer': ['........',
                       '........',
                       '........',
                       '........',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....']
        },
        {
            'input': ['itdoesforitmakesvibrationsintheairanothersaysnoitdoesnotforthere',
                      'ivriatndbortoheerastasynisonootiintsdfooiensrftortihthmeeaakrees'],
            'answer': ['........',
                       '........',
                       '........',
                       '........',
                       'X.X.X.X.',
                       '.X.X.X.X',
                       'X.X.X.X.',
                       '.X.X.X.X']
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofstencilciphergrille',
                      'snsecureacncilcivaptheehesexryarsegroimimfstepplleandilleaboveie'],
            'answer': ['........',
                       '........',
                       '...XXXX.',
                       '...X..X.',
                       '......X.',
                       '......X.',
                       '......X.',
                       'XXXXXXX.']
        },
        {
            'input': ['quickbrownfoxjumpsoverthelazydoggodyzalehtrevospmujxofnworbkciuq',
                      'pgmqodyzsauujxofolnickbrvewoerthorbkhewctrevolniazydsofuoxjupgmq'],
            'answer': ['...X....',
                       '...X....',
                       '...XXXXX',
                       '...X....',
                       '......X.',
                       '......X.',
                       '......X.',
                       'XXXX..X.']
        },
        {
            'input': ['testtesttesttesttesttesttesttestcardcardcardcardcardcardcardcard',
                      'ttcceeaarssrtddtccttaaeesrrsdttdtcctaeearrssddttcttceaaessrrttdd'],
            'answer': ['.X...X..',
                       '..X.X...',
                       '...X...X',
                       'X.....X.',
                       '...X.X..',
                       '..X...X.',
                       '.X.....X',
                       'X...X...']
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofastencilcipherinsuc',
                      'satnvehseneeciecxuryarsimelcpcipmplaleesheaeriboofanvadiesnsituc'],
            'answer': ['..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...']
        },
        {
            'input': ['haciphercertainlettersonapagearepartofthesecretmessagetheyarehid',
                      'ethaespatecisartofgephrsththeroneyesapcearecagrtaieareehnlretmid'],
            'answer': ['..XX....',
                       '..XX....',
                       '....XX..',
                       '....XX..',
                       '......XX',
                       '......XX',
                       'XX......',
                       'XX......']
        },
        {
            'input': ['inthischapterwelookatanumberofciphersystemswhicharebaseduponadif',
                      'iopheraosrnekytsathanumbbisacthseeamrsweodupohnapitdfcceiirwelfh'],
            'answer': ['X.......',
                       '..X...X.',
                       '..X.....',
                       '.XX.X.X.',
                       '..X.....',
                       '........',
                       'X.X....X',
                       '..XXXX..']
        },
        {
            'input': ['ferentideatothosethatwehavemetsofarinthesesystemseachletterretai',
                      'ffareerseaethinactthnwelidhteehtaaevttseeeromsreeyttastsoteihoms'],
            'answer': ['.X...XX.',
                       '..X...X.',
                       '..X.....',
                       'XX...X..',
                       '.X..X...',
                       '...X....',
                       '..X.....',
                       '....XX.X']
        },
        {
            'input': ['nsitsownidentityandsothefrequenciesoftheindividuallettersoftheme',
                      'inansailltsoeedssowthefotfntthreiedeeinqtrsofntihetudivenicdmeuy'],
            'answer': ['.X..X.X.',
                       '.XXX....',
                       '..X.....',
                       '..X.....',
                       'X.X.X.X.',
                       'X......X',
                       '..X.....',
                       '.......X']
        },
        {
            'input': ['ssagesareunchangedbuttheconstituentlettersofthedigraphsandthehig',
                      'sisageedbgrneusareunatctphthhescaondlanstehtttersoefnithiggtheud'],
            'answer': ['X.XXX...',
                       '....X.XX',
                       'XXXX..X.',
                       '...X....',
                       '.....X..',
                       '........',
                       '....X...',
                       '.X......']
        },
        {
            'input': ['herorderpolygraphsareseparatedandtheiroriginalfrequenciesaregone',
                      'hdhsteareesequheeirropriagrnocinrdaatieerpsollygerdaarefgonanepr'],
            'answer': ['X.......',
                       'X.......',
                       '..X.....',
                       '....X...',
                       'XX....X.',
                       'XX.XX.XX',
                       '.X......',
                       '...X..X.']
        },
        {
            'input': ['roughlyspeakinganalgorithmisasequenceofinstructionsthatonemustpe',
                      'ronuuaolensgnthglcyoersoithmfiishapetoneanmkusitsranusegtqpaceti'],
            'answer': ['XX.X....',
                       '...X..X.',
                       'X.X...X.',
                       '........',
                       '..XX....',
                       'X..X..X.',
                       '...X...X',
                       '...X....']
        },
        {
            'input': ['rforminordertosolveawellformulatedproblemwewillspecifyproblemsin',
                      'eldvprpeeacfriobfloerwmymepilrlwnofbeolorweirldmerutllmsaostisno'],
            'answer': ['.....X..',
                       '...X....',
                       '..X.X.X.',
                       '...X....',
                       'X......X',
                       '....X.X.',
                       'XX.X....',
                       '.X...X.X']
        },
        {
            'input': ['termsoftheirinputsandtheiroutputsandthealgorithmwillbethemethodo',
                      'stastawinnelddthrtehelibemsralogfothtriouhtemeetiritphhnutomdpou'],
            'answer': ['....X...',
                       '..X.....',
                       'X.......',
                       '.XX...X.',
                       'X.XX....',
                       '.....X..',
                       'XXX....X',
                       '.....X.X']
        },
        {
            'input': ['theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv',
                      'tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo'],
            'answer': ['X.......',
                       '.X.....X',
                       'X.....XX',
                       '.X..X...',
                       'XX......',
                       '..XXX...',
                       '..X....X',
                       '...X....']
        },
        {
            'input': ['ebiasisasystematicerrorinhowwethinkasopposedtoarandomerrororonet',
                      'ebiaicneidnkarsrisooasmoerraisrypnpoorhoswtewoserdotmaetnteohtar'],
            'answer': ['XX..X...',
                       '....X.X.',
                       'XX......',
                       '...X.X.X',
                       '........',
                       'X.XX....',
                       '....XX.X',
                       '........']
        },
        {
            'input': ['hatsmerelycausedbyourignorancewhereasstatisticalbiasskewsasample',
                      'hbebiyaoreausrsatsikeswsstamgetiresatlycnoarasicanacmusepelwedhl'],
            'answer': ['X.......',
                       '.......X',
                       'XX......',
                       '...X.X..',
                       'XX...XXX',
                       '..X.....',
                       '.....XXX',
                       '.....X..']
        },
        {
            'input': ['sothatitlesscloselyresemblesalargerpopulationcognitivebiasesskew',
                      'eslynigerotteiserpopuvmlahbalettiiebointlasessclseaslcososarkegw'],
            'answer': ['.X......',
                       '.XX.....',
                       '........',
                       '.X.X..X.',
                       'X......X',
                       'X..XXXXX',
                       '........',
                       'XX......']
        },
        {
            'input': ['ourbeliefssothattheylessaccuratelyrepresentthefactsandtheyskewou',
                      'ouctrbstlaheyleenlssayrideftsepsrotecsecnhaheytustkewortuahetefa'],
            'answer': ['XX..XX..',
                       '......X.',
                       '.X.....X',
                       '.XX.X..X',
                       '.XX.....',
                       '.XX.....',
                       '.......X',
                       '........']
        }
    ],
    'Hard': [
        {
            'input': ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb',
                      'ababaaaababbbbbaaaaaaaaaaabaaaaaaabbaaabaabaaaaaaaaaaaaababaabaa'],
            'answer': ['X.....X.',
                       '.......X',
                       'X.XXX.X.',
                       '...X..XX',
                       '......X.',
                       'X.....X.',
                       '......X.',
                       '...X....']
        },
        {
            'input': ['ccccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddd',
                      'dcdccdccccccccdcdccddddcdccddcdcdcdccddcdccccddcccdccdcdddcddcdc'],
            'answer': ['...XX..X',
                       'X.......',
                       '.X.....X',
                       '.....X..',
                       '....X...',
                       '.XXX...X',
                       'X..XX.X.',
                       '........']
        },
        {
            'input': ['acfafcfdfaddeaaefbddcbcbebcaefbecdacdaffdbaebfccbdfdfaeafcbfcdfe',
                      'bdfdfcbacfafcfdfddadafcadebccbeddafecbbafffadcacbdaaebfccfeeefbe'],
            'answer': ['.......X',
                       'XXXXX..X',
                       '...X.X.X',
                       'X......X',
                       '...X....',
                       '...X..X.',
                       '........',
                       '..X.....']
        },
        {
            'input': ['eecdeecafbabcdbdbdfbceccaadabeffacedcafcacdbfcdabceadfabbbefabdb',
                      'bdeefbacbecddccafceececccaaeadabadfaeabcbbefdbfbafbcfcdabdfbdadb'],
            'answer': ['..XX....',
                       '..XX....',
                       '..XX....',
                       'X...X...',
                       '........',
                       '...X...X',
                       'X.XX..X.',
                       'XX......']
        },
        {
            'input': ['xzzwvyzzwvzxyvvyvvxyvzzvvyzxxzwyxywwzzvzzvxvyyzxzvywzvyyzxwvwvwv',
                      'xzvzvvzxywwxyzvyywwvzvzzvzvzyzyzvvzywzxvzwzxvyvxwvxvyyxzvywwyvzx'],
            'answer': ['XX....X.',
                       '..X...X.',
                       'X.......',
                       '.......X',
                       '..X.X..X',
                       'X..X.XX.',
                       '...XX...',
                       '........']
        },
        {
            'input': ['2143224123413143441244344433421141141133321222411132223431211113',
                      '1441414211211443343321332422442343423431211222213214114113114331'],
            'answer': ['.......X',
                       '.X......',
                       '.X.XX...',
                       'X...X...',
                       '........',
                       '.X...X..',
                       'X..XX...',
                       '.XX.XX..']
        },
        {
            'input': ['1423131123444341243321323144211121442322414324433232113143313323',
                      '3122232414233241431131322333212142131444433144243313342442111331'],
            'answer': ['.X.....X',
                       '..X.....',
                       '.X...X..',
                       '.X...X.X',
                       '.X.X.X..',
                       'X......X',
                       '.X.....X',
                       '...X....']
        },
        {
            'input': ['2144231331233214431421223332234434434133144224313244343414433343',
                      '3243132444341434441434134234312313441322123332323223432134434314'],
            'answer': ['.X..X...',
                       '...X....',
                       'X.......',
                       '.X..XX.X',
                       '.....X..',
                       'X....XX.',
                       '.....XXX',
                       '.......X']
        },
        {
            'input': ['4144423434214313311211411134111141342141433134443214134423211112',
                      '4433114124314411234422412413134314423141213141314111133114141234'],
            'answer': ['X...X.X.',
                       '.X...X..',
                       '.....X..',
                       '...X..XX',
                       '......X.',
                       'X..XX...',
                       '.....X..',
                       '..X...X.']
        },
        {
            'input': ['hjgjhjghghhjjggjhhjhjhjhghhhghggggjhghhjjgjjjjgjhhgjjghgjgjjjjhh',
                      'hhhhjhhjgjggjghgjjhhhjjhgjghhhgjgghjjhggjjhjhhgjjjjgghjjggjjhjhg'],
            'answer': ['..X....X',
                       '.....X..',
                       'X...X.X.',
                       'X..X....',
                       'X.......',
                       '....XX..',
                       'XX.XX..X',
                       '........']
        },
        {
            'input': ['lllllllllllllllllllllllllllllllllllllllllllllllllllllmmmmmmmmmmm',
                      'lllllllllllllllllllllmllllllmmllllllllmmllllllmmmmllllllmmllllll'],
            'answer': ['XX......',
                       'XX......',
                       '......XX',
                       '......XX',
                       '....XX..',
                       '....XX..',
                       '..XX....',
                       '..XX....']
        }
    ]
}
