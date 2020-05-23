### This Repository Belongs To: Расолько Юлия Алексеевна

Добро пожаловать на сервис для поиска клиентов для копирайтеров. 
Тут потенциальные клиенты публикуют темы, на которые им нужен текст или выбирают из существующих; копирайтеры добавляют в систему текст и его краткое описание. Для клиентов доступен каталог тем и уже написанные к ним анонсы текстов. За каждого клиента, открывшего полную версию текста, автор получает виртуальные деньги.
***
#### Пример запуска:
- python3 server/main.py - запуск сервера на вашем компьютере
- python3 server/client.py - запуск клиентского приложения
- python3 server/copy-writer.py - запуск приложения для писателей


Далее можно делать запросы в качестве клиента:   get_theme_list, get_demos (просмотр имеющихся демо-версий текстов на интересующую тему), get_full_text, post_new_theme

И в качестве писателя:   get_theme_list, get_money_for_text, post_text
***
#### Для начала можете попробовать выполнить такое взаимодействие:
	client: 
		>Enter command>post_new_theme
		>Which theme would you like to post?> My theme
		>Your theme is now available!
	copy-writer:
		>Enter command>post_text
		>Which theme would you like to post a text on?> My theme
		>Please write here your demo> Here is my demo
		>Please write here your exciting text> Here is my exciting text
		>Your text successfully posted. Its id is 0
	client:
		>Enter command>get_demos
		>Which theme are you interested in?> My theme
		>Here are demos on the theme My theme:  [['Here is my demo', 'text id is 0']]
		>Enter command>get_full_text
		>Which theme are you interested in?> My theme
		>What is the text id?> 0
		>Here is the text:
		>Here is my exciting text
	copy-writer:
		>Enter command>get_money_for_text
		>Which theme is your text written on?> My theme
		>What is the text id?> 0
		>Please get your money:  $
