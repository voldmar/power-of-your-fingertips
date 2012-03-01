Сила ваших кончиков пальцев
===========================

who-am-i: Кто я
---------------
  * Владимир Епифанов
  * @voldmar
  * voldmar@ostrovok.ru
  * разработчик
  * 6 лет FreeBSD, 5 лет Linux
  * 5 лет MacOS X
  * 10 лет vim (и всё ещё учусь)

what-i-want: Почему мне это важно
------------------------


synopsis: О чём рассказ
-----------------------
  * sh, bash, zsh
  * Регулярные выражения
  * sed, awk, find, grep etc

sh
--
  * Голый sh не нужен
  * Везде есть bash
  * Если нет, то поставьте
  * zsh + Oh my zsh
  * Python, Ruby
  * C-X C-E


concepts: Основные концепции
----------------------------
  * Файловая система
  * text in, text out
  * pipes
  * 0 == True

environment-variables: Переменные среды
----------------
  * VAR=value <mark>(*без пробелов!*)</mark>
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
  * pushd, popd, dirs
  * mkdir -p
  * !$

fs-patterns: Паттерны файловой системы
--------------------------------------
  * \*
  * \*\*
  * ?
  * [a-b]
  * [^a-b]

fs-patterns-2: Паттерны файловой системы
--------------------------------------
  * {one,two,three}
  * mv file{,old}
  * python convert.py text.{md,html}

fs-patterns-3: Паттерны файловой системы
--------------------------------------
  * man bash and /Pattern Matching
  * man zshexpn

find
----
  * Обход файловой системы
  * find {path} {predicates}
  * Кавычки
  * xargs

find-2: Предикаты find
-------------
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
  * gsed
  * sed -E
  * sed -n
  * sed -i bak

sed2: Немного полезного
------------------
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

grep-2: Ещё grep
---------
  * grep -q
  * grep -c
  * grep -L # Files without match
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
  * sort -u # *ещё раз*
  * uniq -q
  * uniq -c
  * uniq -d

eg: Exempli gratia
--------------
voldmar@air ~ % awk '{print $2}' history.txt | sort | uniq -c | sort -r | awk '$1 > 20 {print $0}'

eg-2: Exempli gratia
--------------
<pre>
<code>579 ls # Look ma, no mc!</code>
<code>386 git</code>
<code>331 cd  # Look ma, no mc again!</code>
<code>321 brew</code>
<code>280 sd</code>
<code>264 vim # Look ma, no pycharm</code>
<code>113 ssh</code>
</pre>

eg-3: Exempli gratia
--------------
<pre>
<code>78 rm # Ma!..</code>
<code>64 mv</code>
<code>63 man # RTFM</code>
<code>59 .. # Lazy garfield pic</code>
<code>49 cat</code>
<code>47 echo</code>
<code>46 pip</code>
<code>37 which</code>
<code>36 sv</code>
</pre>

eg-4: Exempli gratia
--------------
<pre>
<code>34 grep</code>
<code>30 f</code>
<code>28 mkdir</code>
<code>27 res</code>
<code>24 curl</code>
<code>23 source</code>
<code>23 ipython</code>
<code>21 open</code>
</pre>

aliases: Алиасы и функции
-------------------------
<pre>
<code>alias ..='cd ..'</code>
<code>alias ...='cd ../..'</code>
<code>alias ....='cd ../../..'</code>
</pre>


aliases-2: Алиасы и функции
-------------------------
<pre>
<code>alias cdd='cd $(python -c "import django, os.path; print os.path.dirname(django.__file__)")'</code>
<code>alias g='grep --exclude-dir=.git --exclude=tags -RIEHn'</code>
<code>alias ohwait="git st -s --porcelain -uall | awk '{print \$2}' | grep '[.]py\$' | xargs pyflakes"</code>
<code>alias msh="./manage.py mshell"</code>
<code>alias f="find . -name"</code>
<code>alias F="find . -iname"</code>
<code>alias vd='vim $(git diff --name-only | sort -u)'</code>
</pre>


aliases-3: Алиасы и функции
-------------------------
<pre>
<code>vack () { vim -q<( ack -H --nocolor --nogroup --column  "$@" ); }</code>
<code>mkmig () { ./manage.py schemamigration --auto $1 $2 }</code>
<code>mkdmig () { ./manage.py datamigration $1 $2 }</code>
<code>mig ()  { ./manage.py migrate $1 --ignore-ghost-migrations }</code>
</pre>


aliases-4: Алиасы и функции
-------------------------
<pre>
<code>alias sd="ssh dev2.ostrovok.ru"</code>
<code>alias sv="ssh voldmar.ru"</code>
<code>alias res="while true; do ssh -t dev2.ostrovok.ru proj/ostrota/manage.py runserver 0.0.0.0:8000; sleep 3; done"</code>
<code>alias sres="while true; do ssh -t dev2.ostrovok.ru HTTPS=on proj/ostrota/manage.py runserver 0.0.0.0:8001; sleep 3; done"</code>
<code>alias ipython="python $(which ipython)"</code>
</pre>

io: Ввод-вывод в bash/zsh
------------------------- 
  * \>
  * \>\>
  * <
  * <<

io-2: Ввод-вывод в bash/zsh
------------------------- 
  * <()
     * diff <( cmd1 | cmd2 ) <( cmd3 )
  * \>()
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

macos: Маководам
----------------
  * iTerm 2
  * brew

toread: Почитать
----------------
  * Unix Shell Programming (3rd Edition)
  * Advanced Bash Programming
  * @climagic
  * http://www.catonmat.net/series/sed-one-liners-explained
  * http://www.catonmat.net/series/awk-one-liners-explained

!hiring: Островку нужно ещё больше хороших питонистов!
---------------------------

questions: Вопросы?
------------------

