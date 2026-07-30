#acest proiect am decis sa reprezinte o structura de date care sa retina fapte legate de gestiunea unei liste de redari a unor melodii
#voi implementa un sistem de reguli care pe baza unui input introdus de catre asculataori sa poata recomanda o melodie sau mai multe melodii
#inputul poate sa contina informatii legate de: gen, durata, limba, categorie_public si stare.

#mai intai, cream clasa Melodie care va contine atributele corespunzatoare
class Melodie:
    def __init__(self, nume, artist, gen, durata, limba, categorie_public, stare):
        self.nume=nume
        self.artist=artist
        self.gen=gen
        self.durata=durata
        self.limba=limba
        self.categorie_public=categorie_public
        self.stare=stare
    #adaugam o metoda care verifica, in fct de nr de secunde, daca melodia e scurta, medie sau lunga
    def EsteScurta(self):
        if self.durata<=120: #adica daca melodia e mai scurta sau dureaza chiar 2 minute(120s)
            return "scurta" #returnam o valoare, ne va ajuta cand vom face legatura cu cerintele utilizatorului
        elif self.durata<=240:  #60*4=240 de secunde, 4 min
            return "medie"
        else:
            return "lunga" 
    def estePtCopilasi(self):
        if self.categorie_public=='copii':
             return self.gen=='animat'
          

#acum vom crea o lista de melodii, pe care o vom initializa goala
melodii=[]
#adaugam melodii in lista♥ am o gramadaaa (100), super faine
melodii.append(Melodie('Skyfall', 'Adelle', 'pop-soul', 286, 'engleza', 'adulti', 'trista'))
melodii.append(Melodie('Cai verzi pe pereti', 'Smiley feat. Don Baxter', 'pop-dance', 233, 'romana', 'tineri', 'vesela'))
melodii.append(Melodie('Lovely', 'Billie Eilish feat. Khalid', 'chamber pop', 260, 'engleza', 'tineri', 'melancolica'))
melodii.append(Melodie('Ani de liceu', 'Stela Enache', 'pop', 251, 'romana', 'tineri', 'nostalgica'))
melodii.append(Melodie('S.O.S.', 'Indila', 'indie pop', 288, 'franceza', 'adulti', 'melancolica'))
melodii.append(Melodie('E marfa tare', 'Alex Velea', 'pop', 237, 'romana', 'tineri', 'energica'))
melodii.append(Melodie('Twinkle little star', 'CoComelon', 'animat', 196, 'engleza', 'copii', 'linistita'))
melodii.append(Melodie('Roata Vietii', 'Irina Loghin', 'folclor', 260, 'romana', 'adulti', 'nostalgica'))
melodii.append(Melodie('Earth Song', 'Michael Jackson', 'pop-rock', 404, 'engleza', 'adulti', 'melancolica'))
melodii.append(Melodie('La Gozadera', 'Mark Anthony & Gente de Zona', 'latino pop', 203, 'spaniola', 'adulti', 'energica'))
melodii.append(Melodie('Romania, trezeste-te!', 'Morometzii', 'hip-hop', 298, 'romana', 'adulti', 'melancolica'))
melodii.append(Melodie('Luna', 'Alessandro Safina', 'pop-clasic', 404, 'italiana', 'adulti', 'romanatica'))
melodii.append(Melodie('Un motan cat un pisoi', 'TraLaLa', 'animat', 172, 'romana', 'copii', 'vesela'))
melodii.append(Melodie('Derniere Danse', 'Indila', 'indie pop', 215, 'franceza', 'adulti', 'melancolica'))
melodii.append(Melodie('Let it be', 'The Beatles', 'rock', 243, 'engleza', 'adulti', 'linistita'))
melodii.append(Melodie('Gangsta s Paradise', 'Coolio & L.V.', 'rap', 256, 'engleza', 'tineri si adulti', 'frustranta'))
melodii.append(Melodie('99 problems', 'Jay Z', 'rap', 235, 'engleza', 'adulti', 'frustranta'))
melodii.append(Melodie('Highway to hell', 'AC/DC', 'rock', 208, 'engleza', 'adulti', 'energica'))
melodii.append(Melodie('Coace Doamne prunele', 'Petrica Mitu Stoian', 'populara', 136, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Who is it', 'Michael Jackson', 'pop', 693, 'engleza', 'adulti', 'trista'))
melodii.append(Melodie('Candy Shop', '50 Cent', 'hip-hop', 250, 'engleza', 'tineri si adulti', 'seductiva'))
melodii.append(Melodie('Old Town Road', 'Lil Nas X ft. Billy Ray Cyrus', 'country trap', 158, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Starboy', 'The Weeknd ft. Daft Punk', 'R&B', 274, 'engleza', 'tineri si adulti', 'de aroganta'))
melodii.append(Melodie('Гучи', 'Timati', 'rap', 354, 'rusa', 'adulti', 'vesela'))
melodii.append(Melodie('Baby One More Time', 'Britney Spears', 'pop', 237, 'engleza', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Розовое вино', 'Элджей & Feduk', 'R&B', 203, 'rusa', 'tineri', 'linistita'))
melodii.append(Melodie('Felicita', 'Al Bano & Romina Power', 'pop', 190, 'italiana', 'adulti', 'vesela'))
melodii.append(Melodie('Haideti fetelor la joc!', 'Maria Carneci', 'populara', 149, 'romana', 'adulti', 'energica'))
melodii.append(Melodie('Ride it', 'Jay Sean', 'pop', 189, 'engleza', 'tineri si adulti', 'seductiva'))
melodii.append(Melodie('Bailando', 'Enrique Iglesiasfeat. Descemer Bueno & Gente de Zona', 'latino pop', 287, 'spaniola', 'adulti', 'romantica'))
melodii.append(Melodie('Doi pasi', 'Cargo', 'rock', 210, 'romana', 'tineri si adulti', 'melancolica'))
melodii.append(Melodie('Treat you better', 'Shawn Mendes', 'pop', 257, 'engleza', 'tineri', 'romantica'))
melodii.append(Melodie('Master of Puppets', 'Metallica', 'heavy-metal', 517, 'engleza', 'adulti', 'energica'))
melodii.append(Melodie('No Vaseline', 'Ice Cube', 'hip-hop', 314, 'engleza', 'tineri si adulti', 'agresiva'))
melodii.append(Melodie('Sexy Back', 'Justin Timberlake ft. Timbaland', 'pop-dance', 266, 'engleza', 'tineri si adulti', 'seductiva'))
melodii.append(Melodie('Price Tag', 'Jessie J ft. BoB', 'R&B', 245, 'engleza', 'tineri si adulti', 'vesela'))
melodii.append(Melodie('Dream On', 'Aerosmith', 'rock', 202, 'engleza', 'tineri si adulti', 'melancolica'))
melodii.append(Melodie('Without me', 'Eminem', 'hip-hop', 298, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('In padurea cu alune', 'TraLaLa', 'animat', 121, 'romana', 'copii', 'vesela'))
melodii.append(Melodie('Mary had a little lamb', 'Sarah Joseph Hale', 'animat', 155, 'engleza', 'copii', 'linistita'))
melodii.append(Melodie('Beat it', 'Michael Jackson', 'pop-rock', 299, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Heart-Shaped Box', 'Nirvana', 'metal', 283, 'engleza', 'adulti', 'trista'))
melodii.append(Melodie('California Love', '2pac ft. Dr Dre', 'rap', 412, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Only Human', 'Jonas Brothers', 'raggae-pop', 202, 'engleza', 'tineri si adulti', 'vesela'))
melodii.append(Melodie('Anaconda', 'Nicki Minaj', 'rap', 290, 'engleza', 'adulti', 'vesela'))
melodii.append(Melodie('ТРИ ПОЛОСКИ', 'Davay', 'hardbass', 104, 'rusa', 'adulti', 'energica'))
melodii.append(Melodie('Sorry', 'Justin Bieber', 'pop', 206, 'engleza', 'tineri', 'vesela'))
melodii.append(Melodie('Jesus walks', 'Kanye West', 'hip-hop', 247, 'engleza', 'adulti', 'spirituala'))
melodii.append(Melodie('Agla', 'Pera', 'rock', 231, 'turca', 'tineri si adulti', 'melancolica'))
melodii.append(Melodie('Be the One', 'Dua Lipa', 'pop', 205, 'engleza', 'tineri', 'linistita'))
melodii.append(Melodie('I Know You Want Me', 'Pitbull', 'reggaeton', 247, 'engleza-spaniola', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Narkotik Kal', 'Hardbass School', 'hardbass', 236, 'rusa', 'adulti', 'energica'))
melodii.append(Melodie('I Don t Care', 'Ed Sheeran & Justin Bieber', 'pop', 223, 'engleza', 'tineri', 'vesela'))
melodii.append(Melodie('Smooth Criminal', 'Michael Jackson', 'pop-dance', 258, 'engleza', 'tineri si adulti', 'tensionata'))
melodii.append(Melodie('Aman, aman', 'Keremcem', 'pop', 296, 'turca', 'adulti', 'romantica'))
melodii.append(Melodie('Manifesto', 'Sezen Aksu', 'pop', 211, 'turca', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Hot', 'Inna', 'pop-dance', 222, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Ciorba de curcan', 'Ileana Ciuculete & Puiu Codreanu', 'populara', 185, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Iubire', 'Adriana Antoni', 'pop-folk', 229, 'romana', 'adulti', 'melancolica'))
melodii.append(Melodie('Diggy Down', 'Inna feat. Yandel & Marian Hill', 'pop-dance', 207, 'engleza', 'tineri si adulti', 'senzuala'))
melodii.append(Melodie('Tranquila', 'J Balvin', 'reggaeton', 202, 'spaniola', 'tineri si adulti', 'senzuala'))
melodii.append(Melodie('Fir-ai sa fii bautura!', 'Vladuta Lupau feat. Rapsozii Maramuresului', 'pop-folk', 228, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Eu beau vinul cu borcanu', 'Nicu Paleru', 'de petrecere', 258, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Cliente', 'Inna', 'pop-dance', 209, 'engleza-spaniola', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Yo Te Lo Dije', 'J Blavin', 'reggaeton', 248, 'spaniola', 'tineri si adulti', 'linistita'))
melodii.append(Melodie('Asta da petrecere', 'Claudia Puican', 'de petrecere', 249, 'romana', 'adulti', 'energica'))
melodii.append(Melodie('Prietena mea-i mireasa', 'Vladuta Lupau', 'de petrecere', 204, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Alors On Danse', 'Stromae', 'house', 235, 'franceza', 'tineri si adulti', 'linistita'))
melodii.append(Melodie('O Sen Olsan Bari', 'Aleyna Tilki', 'pop', 189, 'turca', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Mesaj Antidrog', 'LaLa Band', 'pop', 142, 'romana', 'tineri si adulti', 'linistita'))
melodii.append(Melodie('Whenever, Whereever', 'Shakira', 'pop-latino', 199, 'engleza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Bella', 'GIMS', 'pop', 283, 'franceza', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Whistle While You Work', 'Adriana Caselotti', 'animat', 203, 'engleza', 'copii', 'vesela'))
melodii.append(Melodie('Americandrim', 'Puya ft. Connect-R', 'hip-hop', 209, 'romana-engleza', 'tineri si adulti', 'critica'))
melodii.append(Melodie('Change', 'Puya feat. Kamelia & George Hora', 'hip-hop', 287, 'romana-engleza', 'tineri si adulti', 'motivationala'))
melodii.append(Melodie('Hips don t lie', 'Shakira feat. Wyclef Jean', 'pop-latino', 219, 'engleza-spaniola', 'tineri si adulti', 'senzuala'))
melodii.append(Melodie('Tous les memes', 'Stromae', 'pop-dance', 218, 'franceza', 'adulti', 'critica'))
melodii.append(Melodie('Run Rudolph Run', 'Chuck Berry', 'rock and roll', 178, 'engleza', 'toate', 'energica'))
melodii.append(Melodie('Love is the way', 'Connect-R', 'pop-dance', 223, 'engleza', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Cauta-ma', 'Jo & Juno', 'pop', 191, 'romana', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Jingle Bell Rock', 'Bobby Helms', 'rock and roll', 131, 'engleza', 'toate', 'festiva'))
melodii.append(Melodie('Gennie in a Bottle', 'Christina Aguilera', 'pop', 227, 'engleza', 'tineri si adulti', 'senzuala'))
melodii.append(Melodie('My Heart Will Go On', 'Celine Dion', 'pop', 281, 'engleza', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('Undeva-n Balkani', 'Puya', 'hip-hop', 252, 'romana', 'tineri si adulti', 'critica'))
melodii.append(Melodie('Holly Jolly Christmas', 'Michael Buble', 'jazz-pop', 122, 'engleza', 'toate', 'linistita'))
melodii.append(Melodie('Barbie Girl', 'Aqua', 'electropop', 202, 'engleza', 'tineri', 'vesela'))
melodii.append(Melodie('Rockin Around', 'Brenda Lee', 'rock and roll', 129, 'engleza', 'toate', 'toate'))
melodii.append(Melodie('O Sole Mio', 'Alfredo Mazzucchi & Eduardo DiCapua', 'opera', 202, 'italiana', 'adulti', 'romantica'))
melodii.append(Melodie('Dota', 'Basshunter', 'eurodance', 236, 'suedeza', 'tineri si adulti', 'energica'))
melodii.append(Melodie('Se muta soacra la noi', 'Varu Sandel si Simona Boncut', 'de petrecere', 260, 'romana', 'adulti', 'vesela'))
melodii.append(Melodie('Oac Oac Diri Diri Dam', 'HeyKids', 'animat', 69, 'romana', 'copii', 'energica'))
melodii.append(Melodie('Zitti e Buoni', 'Maneskin', 'rock', 199, 'italiana', 'adulti', 'energica'))
melodii.append(Melodie('Baby Shark', 'Pinkfong', 'animat', 80, 'engleza', 'copii', 'vesela'))
melodii.append(Melodie('Menta Ma', 'Mc Staff, Nakama', 'electronic', 74, 'portugheza', 'tineri si adulti', 'linistita'))
melodii.append(Melodie('Ce sa-ti mai cer, Doamne, Tie?', 'Constantin Enceanu', 'populara', 301, 'romana', 'adulti', 'linistita'))
melodii.append(Melodie('Asa trec zilele mele', 'Maria Dragomiroiu', 'populara', 269, 'romana', 'adulti', 'melancolica'))
melodii.append(Melodie('Sa Cante Trompetele', 'B.U.G. Mafia feat. Feli', 'hip-hop', 448, 'romana', 'tineri si adulti', 'energica'))
melodii.append(Melodie('S-a marit armata', 'Albatros', 'de petrecere', 228, 'romana', 'adulti', 'melancolica'))
melodii.append(Melodie('Ochii Tai', 'L.A.', 'pop-dance', 223, 'romana', 'tineri si adulti', 'romantica'))
melodii.append(Melodie('De Ziua Ta', '3 Sud Est', 'pop-dance', 246, 'romana', 'tineri si adulti', 'festiva'))
#acum vom determina inputul de la utilizator
user_gen=input("Genul melodiei: pop/rock/heavy metal/rap/animat etc ")
user_durata=input("Durata melodiei sa fie: scurta/medie/lunga ")
user_limba=input("Limba in care se canta melodia: ")
user_categorie_public=input("Categoria de public careia i se adreseaza melodia: copii/tineri/adulti ")
user_stare=input("Starea pe care o transmite melodia este una: trista/vesela/energica/malnacolica/romantica/nostalgica/linistita ")

#facem verificarea, adica setam regulile: daca o melodie respecta criteriile ascultatorului, o recomandam
def se_recomanda(melodie, gen, durata, limba, categorie_public, stare): #dupa fiecare "si" vom pune o \ ca sa separam fiecare rand, practic sa incepem de la capat, unele sub altele asa
    #imi doresc ca userul sa poata alege melodii in functie de cate criterii vrea el; adica sa nu introduca neaparat toate atributele, de exe poate vrea doar genul sau doar o anumita limba
    #pentru asa vom pune spatiu gol daca atributul nu il intereseaza pe ascultator, iar in caz ca isi doreste sa aleaga pe baza atributului, sa poata introduce; vom folosi deci, cate un "sau" la fiecare
    #pentru fiecare pereche de "sau" vom pune totul in paranteze, pt ca "si" are prioritate mai mare decat "sau" si altfel s-ar interpreta gresit, s-ar face o comparatie si ar iesi toate True
    if (gen=='' or melodie.gen==gen) and \
        (durata=='' or melodie.EsteScurta()==durata) and \
        (limba=='' or melodie.limba==limba) and \
        (categorie_public=='' or melodie.categorie_public==categorie_public) and \
        (stare=='' or melodie.stare==stare):
            print("Melodia respecta criteriile utilizatorului♥")                
            return True

#ne ramane sa aplicam regulile create: cream o lista vida de recomandari si adaugam melodiile care se potrivesc cu cerintele userului
recomandari=[]

#parcurgem fiecare melodie din lista de melodii si verificam daca functia se_recomanada este adevarata; daca este adevarata, adaugam acea melodie in lista de recomanadari
for melodie in melodii:
    if se_recomanda(melodie, user_gen, user_durata, user_limba, user_categorie_public, user_stare)==True:
        recomandari.append(melodie)

#afisam un mesaj pentru user, unde el sa introduca ce doreste♥
if recomandari: #adica daca exista vreo recomandare, daca ceva s-a "pupat" cu cerintele, atunci:
    print("Pe baza preferintelor, va recomandam melodia/melodiile:")
    for melodie in recomandari: #pentru melodia/melodiile care se afla in lista de recomanadari, vom afisa numele si artistul/artistii
        print(' ♥ ', melodie.nume, ', de', melodie.artist) #punem un ', de' de legatura intre numele melodiei si artist; virgula o punem inainte de "de" si dupa melodie, sa arate si corect gramatical ♥
        
        

    
        
    
        