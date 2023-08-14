import time
import Masiv
import Algoritms

blok = Masiv.blok
Bubbles = Algoritms.bubble_sort
Selection = Algoritms.selection_sort
Shuffle = Algoritms.shuffle_sort
Shell = Algoritms.shell_sort
Quick = Algoritms.quick_sort
Merge = Algoritms.merge_sort

#Засекает время создания масива и работи алгоритма.
def taimer (Bubbles, Selection, Shuffle, Merge, Quick, Shell, blok):
    n = [Quick, Bubbles, Selection, Shuffle, Merge, Shell]
    for i in range(len(n)):
        start_time = time.time();
        blokAlgoSorted = n[i](blok);
        end_time = time.time();
        elapsed_time = end_time - start_time
        print(f"Прошло {elapsed_time} секунд.");
        i = i + 1
    blok.sort();
    blokSorted = list(blok);
    print(blokAlgoSorted == blokSorted);
taimer(Bubbles, Selection, Shuffle, Merge, Quick, Shell, blok)
