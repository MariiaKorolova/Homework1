#1. Зарегистрироваться на GitHub или GitLab
#2. Подключить учетную запись к PyCharm (задачи, перечисленные, ниже загрузить в свой репозиторий)

#3. Ввести в консоле

 import antigravity
 import __hello__
 from __future__ import braces

#4. Вывести на консоль своё имя, нарисованное 'звёздочками'. Для выполнения этого задания надо использовать не только
символы звёздочки и пробела, но и ESCAPE символы: \n и \t

*       *         *         *       * *********
**      *        * *        **     ** *
* *     *       *   *       * *   * * *
*  *    *      *     *      *  * *  * *******
*   *   *     *       *     *   *   * *
*    *  *    ***********    *       * *
*     * *   *           *   *       * *
*      **  *             *  *       * *
*       * *               * *       * **********

def printM():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height + 1):
            if (j == height):
                print("*", end="")
            elif (j == counter or j == height - counter - 1):
                print("*", end="")
            else:
                print(end=" ")
        if (counter == height // 2):
            counter = -99999
        else:
            counter = counter + 1

        print()


def printA():
    n = width // 2
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n - 1
def printR() :
    half = (height // 2)
    for i in range(0,height) :
        print("*",end="")
        for j in range(0,width) :
            if ( (i == 0 or i == half) and j < (width - 2) ):
                print("*",end="")
            elif ( j == (width - 2) and not(i == 0 or i == half) ) :
                print("*",end="")
            else :
                print(end=" ")
        print()


def printI(height=None):
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printI():
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printA():
    n = width // 2
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n - 1


#5. Написать программу, которая выводит в консоль таблицу Escape-последовательностей:

Escape sequences
\a      Bell (alert)
\b      Backspace
\n      New line
\t      Horizontal tab
\\      Backslash \
\"      Double quotation mark "
\'      Single quotation mark '

print(
    'Escape sequences\n'
    '\\a - Bell (alert)\n',
    '\r\\b - Backspace\n',
    '\r\\n - New line\n',
    '\r\\t - Horizontal tab\n',
    '\r\\\ - Backslash \\\n'
    '\r\\" - Double quotation mark \"\n'
    '\r\\\' - Single quotation mark \'\n'
    'test'
    )