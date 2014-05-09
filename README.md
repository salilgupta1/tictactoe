tictactoe
=========
We are using python3 to implement minimax and alpha-beta pruning

The default function, <code>play()</code> is set to running with alpha-beta pruning with the computer as the player O

In order to run type
<code>python3 TicTacToe.py</code>

If you would like to make the computer player X change the code of main from <code>play()</code> to <code>playAsO()</code>

If you would like to change from alpha-beta pruning to minimax change lines 84 and 103 from
<code>ab_decision(Board,cpuval)</code> to <code>minimax(Board,cpuval)</code>
to change the <code>play()</code> and <code>playAsO()</code> functions respectively.
