<p>
<i>
Это четвертая миссия на тему классической криптографии. В этой миссии нам предстоит взломать шифр "Поворотная решетка". Чтобы узнать больше про этот шифр, настоятельно рекомендуется пройти миссии <a href="https://py.checkio.org/mission/cipher-map2/">Cipher Map</a> и <a href="https://py.checkio.org/mission/rotating-grille-cipher/">Rotating Grille Cipher</a>.
</i>  
</p>


<p>
<i>Атака на основе открытого текста</i> (<i>Known Plaintext Attack</i>,  <i>KPA</i>) - такой вид криптоанализа, когда аналитику известны как шифртекст, так и открытый текст соответствующего ему сообщения. Используя эти тексты, аналитик может получить ключ шифрования и дешифровать другие сообщения, закрытые тем же ключом. В некоторых случаях взлом шифра при известном открытом тексте тривиален: например, шифр Цезаря можно взломать, зная лишь один символ открытого текста и соответствующий ему символ криптограммы. В других случаях процесс подбора ключа может быть более сложным.
</p>

<p>
В этом задании вы попробуете придумать атаку на основе открытого текста для шифра "Поворотная Решетка". Вкратце напомним алгоритм: ключом шифрования является квадратный трафарет с вырезанными отверстиями (в этой миссии используются решетки размера 8х8); отправитель кладет трафарет на лист бумаги и вписывает в прорези первые 16 букв сообщения, затем поворачивает трафарет на 90 градусов по часовой стрелке, вписывает вторые 16 букв и так далее, пока не будет заполнен весь лист. Получателю сообщения нужно выписать криптограмму в квадрат 8х8 и, поочередно прикладывая решетку четырьмя сторонами, прочитать буквы в прорезях.
</p>
<p>
Нам даны две строки: открытое сообщение и соответствующая этому сообщению криптограмма. Оба текста имеют длину 64 символа. Нужно найти ключ (решетку), которая была использована для зашифрования сообщения. Как и в предыдущих заданиях, ключ должен быть представлен в виде списка строк, где "Х" соответствует отверстию в решетке, а "." - тому, что прорези нет.
</p>
<p>
Важное замечание: каждый пример в этой миссии гарантировано имеет одно-единственное решение.
</p>

<p>
    <strong>Входные данные: </strong> открытый текст в виде строки, криптограмма в виде строки 
</p>

<p>
    <strong>Выходные данные: </strong> ключ в виде списка строк
</p>


<!-- Give some usage examples -->
<div class="for_info_only">
    <p>
        <strong>Пример:</strong>
    </p>
<pre class="brush: python">
find_grille('weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong',
            'wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz') == ['X...X...',
                                                                                    '.X.....X',
                                                                                    '..X...X.',
                                                                                    '...X.X..',
                                                                                    'X.....X.',
                                                                                    '...X...X',
                                                                                    '..X.X...',
                                                                                    '.X...X..']                                   
</pre>
</div>


<p>
    <strong>Условия:</strong><br>
    len(plaintext) == 64<br>
    len(cryptogram) == 64<br>
    len(key) == 8<br>
    all(len(line) == 8 for line in key)<br>
    all(all(cell == "X" or cell == "." for cell in line) for line in key)<br>
</p>
