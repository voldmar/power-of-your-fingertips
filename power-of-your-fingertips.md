Сила ваших кончиков пальцев
===========================

who-am-i: Кто я
---------------
  * Владимир Епифанов
  * @voldmar
  * разработчик
  * 6 лет FreeBSD, 5 лет Linux
  * 5 лет MacOS X
  * 10 лет vim (и всё ещё учусь)

what-i-want: Почему мне это важно
------------------------
  * img: baby fingers
  * img: monk


synopsis: О чём рассказ
-----------------------
  * sh, bash, zsh
  * Регулярные выражения
  * sed, awk, find, grep etc
  * ssh
  * tmux
  * vim

sh
--
  * Голый sh не нужен
  * Везде есть bash
  * Если нет, то поставьте
  * zsh + Oh my zsh
  * Python, Ruby


concepts: Основные концепции
----------------------------
  * Файловая система
  * text in, text out
  * pipes
  * 0 == True 

environment-variables: Переменные среды
----------------
  * VAR=value (*без пробелов!*)
  * наследование
  * export
  * передача параметров через переменные
  * наоборот нельзя

fs: Файловая система
--------------------
  * Иерархия
  * Права
  * $HOME, $PWD, $OLD_PWD
  * cd
  * cd -
  * pushd, popd
  * mkdir -p

fs-patterns: Паттерны файловой системы
--------------------------------------
  * \*
  * \*\*
  * ?
  * [a-b]
  * [^a-b]
  * {one,two,three}
  * mv file{,old}
  * man bash and /Pattern Matching
  * man zshexpn

find
----
  * Обход файловой системы
  * find {path} {predicates}
  * Кавычки
  * xargs
  * -name
  * -iname
  * -ftype
  * -newer
  * -delete (только для файлов)
  * -exec
  * -depth, -maxdepth, -mindepth
  * man find

re: Регулярные выражения
--------------------
  * a
  * (a|b)
  * a?
  * a*
  * a+
  * a*?
  * [a-z]

sed
---
  * ed
  * sed -E
  * sed -n
  * sed -i bak
  * s/foo/bar/
  * s/(foo)bar/baz\1/
  * /start/,/end/s/foo/bar/g
  * 1,/end/s/foo/bar/g
  * man sed

awk
---
  * CSV et al.
  * awk -F
  * pattern { action }
  * {print $2, $1}
  * man awk

grep
----
  * grep
  * grep -HRIEn
  * grep -i
  * grep -e
  * grep -f
  * grep -v
  * grep -q
  * grep -c
  * grep -L # TODO: GNU grep?
  * grep -o
  * grep -A, grep -B, grep -C
  * ack

sort
----
  * sort -u
  * sort -n
  * sort -t

uniq
----
  * uniq -q
  * uniq -c

Exempli gratia 23
--------------
<pre>
voldmar@air ~ % awk '{print $2}' history.txt | sort | uniq -c | sort -r | awk '$1 > 20 {print $0}'
 579 ls # Look ma, no mc!
 386 git
 331 cd  # Look ma, no mc again!
 321 brew
 280 sd
 264 vim # Look ma, no pycharm
 113 ssh
  78 rm # Ma!..
  64 mv
  63 man # RTFM
  59 .. # Lazy garfield pic
  49 cat
  47 echo
  46 pip
  37 which
  36 sv
  34 grep
  30 f
  28 mkdir
  27 res
  24 curl
  23 source
  23 ipython
  21 open
</pre>

aliases: Алиасы и функции
-------------------------
  * alias ..='cd ..'
  * alias ...='cd ../..'
  * alias ....='cd ../../..'
  * alias cdd='cd $(python -c "import django, os.path; print os.path.dirname(django.__file__)")'
  * alias g='grep --exclude-dir=.git --exclude=tags -RIEHn'
  * alias ohwait="git st -s --porcelain -uall | awk '{print \$2}' | grep '[.]py\$' | xargs pyflakes"
  * alias msh="./manage.py mshell"
  * alias f="find . -name"
  * alias F="find . -iname"
  * alias vd='vim $(git diff --name-only | sort -u)'
  * vack () { vim -q<( ack -H --nocolor --nogroup --column  "$@" ); }

  * mkmig () { ./manage.py schemamigration --auto $1 $2 }
  * mkdmig () { ./manage.py datamigration $1 $2 }
  * mig ()  { ./manage.py migrate $1 --ignore-ghost-migrations }
  * alias sd="ssh dev2.ostrovok.ru"
  * alias sv="ssh voldmar.ru"
  * alias res="while true; do ssh -t dev2.ostrovok.ru proj/ostrota/manage.py runserver 0.0.0.0:8000; sleep 3; done"
  * alias sres="while true; do ssh -t dev2.ostrovok.ru HTTPS=on proj/ostrota/manage.py runserver 0.0.0.0:8001; sleep 3; done"
  * alias ipython="python $(which ipython)"

io: Ввод-вывод в bash/zsh
------------------------- 
  * >
  * >>
  * <
  * <<
  * <()
     * diff <( cmd1 | cmd2 ) <( cmd3 )
  * $()
  * $(( ))

flow: Управление
----------------
  * for
  * [ ]  # Пробел!
  * [[ ]]
  * &&, ||
  * {}
  * ()
  * &, wait

ssh
---
  * Ключи
  * ssh-add
  * .ssh/config #TODO: check options
  
        Host *
            ForwardAgent yes
            ServerAliveInterval 20
            ControlPersist 4h
            TcpKeepAlive no
            ExitOnForwardFailure yes
            ConnectTimeout 10

        Host verysecure.example.org
            IdentityFile ~/.ssh/secure_key 
            Port 29418

  * ssh -t
  * TODO: туннель
  * ssh -fN -R 8022:localhost:22 dev2.ostrovok.ru
  * TODO: sd cat .ssh/config

tmux
----
  * Отдельная тема

vim
---
  * Отдельная большая тема

macos: Маководам
----------------
  * iTerm 2
  * brew

toread: Почитать
----------------
  * Зелёная книга
  * Advanced Bash Programming
  * Твитер


questions: Вопросы?
------------------

