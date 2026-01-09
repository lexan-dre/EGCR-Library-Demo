import tkinter as tk
import sqlite3

# создание локальной базы данных

db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
    id BIGINT PRIMARY KEY,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Year_published INT NOT NULL,
    Link TEXT NOT NULL
    );
''')

# загрузка книг

books = [
    (1, "Acta Latina Concilii Florentini, quae edidit Georgius Hofmann", 'Andreas de Santacroce, advocatus consistorialis', 1955, 'Andreas de Santacroce, advocatus consistorialis, Acta Latina Concilii Florentini, quae edidit Georgius Hofmann S.I., Romae 1955, vol. vi, p. 288'),
    (2, 'Les “Mémoires” du Grand Ecclésiarque de l’Église de Constantinople Sylvestre Syropoulos sur le Concile de Florence (1438-1439)', 'V. Laurent', 1971, 'V. Laurent, Les “Mémoires” du Grand Ecclésiarque de l’Église de Constantinople Sylvestre Syropoulos sur le Concile de Florence (1438-1439), Roma 1971, vol. ix, p. 715'),
    (3, 'История Флорентийского собора', 'Остроумов, И.Н.', 1847, 'Остроумов, И.Н. История Флорентийского собора / магистерская диссертация, переработанная проф. А В. Горским. М.: В Тип. А. Семена, 1847. 214 с (Санкт-Петербург, Общество памяти игумена Тихона, 2015.)'),
    (4, 'Митрополит Исидор Киевский (1385/1390-1463)', 'Акишин С. Ю.', 2018, 'Акишин С. Ю. Митрополит Исидор Киевский (1385/1390-1463). — Екатеринбург: Екатеринбургская духовная семинария, 2018. — 324 с. — ISBN 978-5-6041842-0-2'),
    (5, 'Cardinal Isidore, c. 1390–1462: A Late. Byzantine Scholar, Warlord, and Prelate', 'Philippides Marios, Hanak Walter K.', 2018, 'Philippides Marios, Hanak Walter K. Cardinal Isidore, c. 1390–1462: A Late. Byzantine Scholar, Warlord, and Prelate. London and New York: Routledge, 2018. Pp. xii, 421'),
    (6, 'Софья Палеолог', 'Татьяна Матасова', 2017, 'Софья Палеолог / Татьяна Матасова. - 2-е изд., исправленное. - Москва : Молодая гвардия, 2017. - 299, [2] с., [16] л. ил. - (Жизнь замечательных людей ; вып. 1635'),
    (7, 'Аристотель Фьораванти', 'Земцов С. М., Глазычев В. Л.', 1985, 'Земцов С. М., Глазычев В. Л. Аристотель Фьораванти. М.: Стройиздат, 1985. 184 с.'),
    (8, 'Из Смутного времени: Лжедмитрий I и его связи с папским престолом', 'Пирлинг П.О.', 2016, 'Пирлинг П.О. Из Смутного времени: Лжедмитрий I и его связи с папским престолом. Изд. 2. 2016. 288 с.'),
    (9, 'Исторические сочинения о России XVI века', 'Поссевино А.', 1983, 'Поссевино А. Исторические сочинения о России XVI века. – М., 1983, с. 272'),
    (10, 'Католические церкви, часовни и духовенство в Российской империи по состоянию на 1917 г. и в советский период в Могилёвской архиепархии', 'Пожарский Христофер', 2021, 'Пожарский Х. Католические церкви, часовни и духовенство в Российской империи по состоянию на 1917 г. и в советский период в Могилёвской архиепархии Санкт-Петербург: Свое издательство, и Тираспольской епархии. Книга Памяти. 2021. - 696 с., цветной вкладыш (64 с.). ISBN 978-5-4386-1986-4'),
    (11, 'Католики в Кузбассе. XVII-XX вв. Очерк истории, документы и материалы', 'Ханевич В.А.', 2009, 'Ханевич В.А. Католики в Кузбассе. XVII-XX вв. Очерк истории, документы и материалы. Кемерово: 2009. — 347 с. ISBN 978-5-91719-2'),
    (12, 'Польские экспонаты и особо ценные документы в музеях, архивах, библиотеках и костёлах Санкт-Петербурга. Путеводитель – информатор', 'Пожарский Христофер', 2016, 'Христофер Пожарский «Польские экспонаты и особо ценные документы в музеях, архивах, библиотеках и костёлах Санкт-Петербурга. Путеводитель – информатор». Варшава – Санкт-Петербург 2016, 144 с.'),
    (13, 'La princesse Zénaide Wol-konsky de la Russie impériale à la Rome des papes', 'Trofimoff André', 1966, 'Trofimoff André. La princesse Zénaide Wol-konsky de la Russie impériale à la Rome des papes. Rome: Staderini, 1966 - c. 64.'),
    (14, 'Католическая церковь в Башкирии: История и современность', 'Симонов В.В.', 2003, 'Симонов В.В. Католическая церковь в Башкирии: История и современность. Уфа: Изд. центр "Орел", 2003. - 64 с.: ил.'),
    (15, 'Памяти 425 католических священников разных национальностей и обрядов, погибших в тюрьмах, лагерях и ссылках (1918-1958 гг.)', 'Пожарский Христофер', 2018, 'Пожарский Х. Памяти 425 католических священников разных национальностей и обрядов, погибших в тюрьмах, лагерях и ссылках (1918-1958 гг.). СПб, 2018 г. - 32 с.'),
    (16, 'История Евангелическо-Лютеранской церкви на Северо-Западе России (1917-1945 гг.)', 'Шкаровский М. В.', 2004, 'Шкаровский, М. В. История Евангелическо-Лютеранской церкви на Северо-Западе России (1917-1945 гг.) / М. В. Шкаровский, Н. Ю. Черепенина. — Санкт-Петербург : Дмитрий Буланин, 2004. — 384 с. ISBN 5-86007-443-3.'),
    (17, 'Антонио Ринальди', 'Кючарианц Д. А.', 1984, 'Антонио Ринальди / Д. А. Кючарианц. — Л.: Стройиздат, Ленингр. отд-ние, 1984. — 176 с., ил. —(Мастера архитектуры).'),
    (18, 'П. Я. Чаадаев в русской культуре двух веков', 'Гурвич-Лищинер С. Д.', 2006, 'П. Я. Чаадаев в русской культуре двух веков / С. Д. Гурвич-Лищинер ; Тель-Авивский ун-т. - Санкт-Петербург : Нестор-История, 2006. - 251, [1] с.; 20 см.'),
    (19, 'Gabrijel Gruber: od ljubljanskega prekopa do jezuitskega generala', 'Stanislav Juznic', 2006, 'Gabrijel Gruber: od ljubljanskega prekopa do jezuitskega generala/ Stanislav Juznic. – Ljubljana: Druzina, 2006. – 216 с.: ил., портр., табл., факс.; 30 с. ISBN 978-961-222-607-7.'),
    (20, 'История Мальтийского ордена', 'Захаров В. А., Чибисов В. Н.', 2012, 'История Мальтийского ордена / В.А. Захаров, В.Н. Чибисов. — Москва : Вече, 2012. — 412, [3] с., [8] л. ил.; 21. — (Гриф секретности снят, История орденов и тайных обществ); ISBN 978-5-9533-5258-1.'),
    (21, 'Velehradský unionismus: cyrilometodějská idea jednoty v různosti', 'Petr Hudec', 2023, 'Velehradský unionismus: cyrilometodějská idea jednoty v různosti/ Petr Hudec velehrad, Matice velehradská, 2023 - 144. pp/ ISBN 8088414040, 9788088414049'),
    (22, 'Рэпрэсаваныя каталіцкія духоўныя, кансэкраваныя і свсцкія асобы Беларусі', 'Леанід Маракоў', 2009, 'Рэпрэсаваныя каталіцкія духоўныя, кансэкраваныя і свсцкія асобы Беларусі (1917—1964) / Леанід Маракоў.:Смэлтак — Мінск, 2009 — 776 с. ISBN 978-985-6917-12-0.'),
    (23, 'Yo escogí la libertad', 'Victor Kravchenko', 2008, 'Yo escogí la libertad /Victor Kravchenko. Madrid : Ciudadela, 2008 - 491 pp. ISBN 978-84-96836-24-2'),
    (24, 'Una difficile transizione. Il cattolicesimo tra unionismo ed ecumenismo (1952-1964)', 'Mauro Velati', 1996, 'Mauro Velati, Una difficile transizione. Il cattolicesimo tra unionismo ed ecumenismo (1952-1964), Il Mulino, Bologna 1996, pp. 504. ISBN 88-15-05467-7'),
    (25, 'Юрий Крижанич : очерк жизни и творчества', 'Пушкарев Л. Н.', 1984, 'Юрий Крижанич : очерк жизни и творчества / Л. Н. Пушкарев ; ответственный редактор доктор исторических наук В. И. Буганов ; Академия Наук СССР, Институт истории СССР. - Москва : Наука, 1984. - 212, [1] с.; 23 см.'),
    (26, 'История Католической Церкви на Астраханской земле', 'отец Вальдемар Мацкевич', 2012, 'История Католической Церкви на Астраханской земле / отец Вальдемар Мацкевич (OFM Conv). - Астрахань: ООО «Типография «Новая Линия», 2012. – 248 с., [20]с. ил.')
]

cursor.executemany(
    "INSERT OR IGNORE INTO Books VALUES(?, ?, ?, ?, ?);",
    books)

db.commit()
db.close()

# нужные функции

def search():
    keyword = entry.get().strip()
    listbox.delete(0, tk.END)
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM Books 
        WHERE Link LIKE ?;
        ''', ('%' + keyword + '%',)
                   )
    results = cursor.fetchall()

    db.commit()
    db.close()
    for result in results:
        listbox.insert(tk.END, result)


def display():
    listbox.delete(0, tk.END)
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Books')
    rows = cursor.fetchall()
    db.close()
    for row in rows:
        listbox.insert(tk.END, row[0], row[4])


# код самого приложения

root = tk.Tk()
root.title('Библиотека РКЦВО')
root.geometry('700x700')

label1 = tk.Label(root, text='Введите запрос в поле поиска')
label1.pack(side='top', pady=50)
entry = tk.Entry(root, width=55)
entry.pack(side='top', pady=70)

search_button = tk.Button(root, text='Поиск', command=search)
search_button.pack(side='top', padx=70, pady=20)

display_button = tk.Button(root, text='Показать все', command=display)
display_button.pack(side='top', padx=70, pady=10)

listbox = tk.Listbox(root, width=70, height=40)
listbox.pack(pady=10)

root.mainloop()
