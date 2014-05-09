tictactoe
=========
We are using Python 3 to implement minimax and alpha-beta pruning (though our program will run with Python 2 as well).

The default function, <code>play()</code>, is set to run with the computer as player O, using minimax with alpha-beta pruning.

In order to run, type <code>python3 TicTacToe.py</code>.

If you would like to make the computer player X, change the code in <code>main()</code> from <code>play()</code> to <code>playAsO()</code>.

If you would like to change from alpha-beta pruning to vanilla minimax, change lines 84 and 103 from
<code>ab_decision(Board,cpuval)</code> to <code>minimax(Board,cpuval)</code>
to change the <code>play()</code> and <code>playAsO()</code> functions respectively.
