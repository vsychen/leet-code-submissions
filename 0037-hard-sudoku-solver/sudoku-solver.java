import java.util.ArrayList;
import java.util.List;

class Solution {
    // TOPICS: MATRIX/BACKTRACKING
    // Test all possible combinations until the correct combination is found. For each position (i,j) check the same row, same column and same square
    // for the numbers already placed; make the choices list the numbers not found in them. For each possible choice, check the next '.' character and
    // its possibilities. If the matrix goes all the way to the end (i=9,j=9), the valid answer has been found; If a null matrix has returned, the
    // combination is invalid, try other combination.
    public List<Character> getRow(char[][] board, int i) {
        List<Character> r = new ArrayList<>();
        for (int j = 0; j < board[i].length; j++) if (board[i][j] != '.') r.add(board[i][j]);
        return r;
    }

    public List<Character> getColumn(char[][] board, int j) {
        List<Character> r = new ArrayList<>();
        for (int i = 0; i < 9; i++) if (board[i][j] != '.') r.add(board[i][j]);
        return r;
    }

    public List<Character> getSquare(char[][] board, int i, int j) {
        int x = i/3;
        int y = j/3;
        List<Character> r = new ArrayList<>();
        for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) if (board[x*3+a][y*3+b] != '.') r.add(board[x*3+a][y*3+b]);
        return r;
    }

    public List<Character> getChoices(List<Character> lst1, List<Character> lst2, List<Character> lst3) {
        List<Character> choices = new ArrayList<>(List.of('1','2','3','4','5','6','7','8','9'));
        for (Character elem : lst1) if (choices.contains(elem)) choices.remove(elem);
        for (Character elem : lst2) if (choices.contains(elem)) choices.remove(elem);
        for (Character elem : lst3) if (choices.contains(elem)) choices.remove(elem);

        return choices;
    }

    public char[][] nextMove(char[][] board, int i, int j) {
        int nextI = (j == 8) ? i+1 : i;
        int nextJ = (j == 8) ? 0 : j+1;

        if (i >= 9 || j >= 9) return board;
        else if (board[i][j] != '.') {
            if (i == 8 && j == 8) return board;
            else return nextMove(board, nextI, nextJ);
        } else {
            List<Character> choices = getChoices(getRow(board, i), getColumn(board, j), getSquare(board, i, j));

            if (choices.isEmpty()) return null;
            char[][] aux = null;

            for (Character choice : choices) {
                board[i][j] = choice;
                aux = nextMove(board, nextI, nextJ);

                if (aux == null) board[i][j] = '.';
                else {
                    break;
                }
            }

            return aux;
        }
    }

    public char[][] solveSudoku(char[][] board) {
        char[][] r = nextMove(board, 0, 0);
        return r;
    }
}