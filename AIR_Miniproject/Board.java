import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Board {

	int N;
	int[] board;
	
	Board(int board[])
	{
		N = (int) Math.sqrt((double)board.length);
		this.board = new int[board.length];
		for(int i=0;i<N*N;i++)
		{
			this.board[i] = board[i];
		}
	}
	
	Board(int[][] blocks)
	{
		N = blocks[0].length;
		board = new int[N*N];
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				this.board[i*N+j]=blocks[i][j];
			}
		}
	}
	
	public boolean isGoal()
	{
		for(int i=0;i<N*N-1;i++)
		{
			if(board[i]!=i+1)
				return false;
		}
		return true;
	}
	public Board exch(Board a, int i, int j)
	{
		int temp = a.board[i];
		a.board[i]=a.board[j];
		a.board[j]=temp;
		return a;
	}
	public Iterable<Board> neighbours()
	{
		Queue<Board> b = new LinkedList<Board>();
		int index=0;
		Board neighbour;
		for(int i=0;i<board.length;i++)
		{
			if(board[i]==0)
			{
				index=i;
				break;
			}
		}
		
		if(index/N !=0) //Not topmost row
		{
			neighbour = new Board(board);
			neighbour = exch(neighbour, index, index-N);
			b.add(neighbour);
		}
		if(index/N !=(N-1)) //Not bottom-most row
		{
			neighbour = new Board(board);
			neighbour = exch(neighbour, index, index+N);
			b.add(neighbour);
		}
		if(index%N !=0) //Not leftmost column
		{
			neighbour = new Board(board);
			neighbour = exch(neighbour, index, index-1);
			b.add(neighbour);
		}
		if(index%N !=(N-1)) //Not rightmost column
		{
			neighbour = new Board(board);
			neighbour = exch(neighbour, index, index+1);
			b.add(neighbour);
		}
		
		return b;
		
	}
	
	public boolean equals(Object y)
	{
		if(y == this) return true;
		if(y == null) return false;
		if(y.getClass() != this.getClass()) return false;
		
		Board that  = (Board)y;
		return (Arrays.equals(that.board, this.board));
			
		
	}
	public int manhatton()
	{
		int sum=0;
		for(int i=0;i<N*N;i++)
		{
			if(board[i]!=i+1 && board[i]!=0)
			sum += manhatton(board[i], i);
		}
		return sum;
	}
	public int manhatton(int goal, int current)
	{
		int row, col;
		row= Math.abs((goal-1)/N - current/N);
		col = Math.abs((goal-1)%N - current%N);
		
		return row+col;
	}
}
