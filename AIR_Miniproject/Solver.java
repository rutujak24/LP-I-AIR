import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Stack;

public class Solver {

	private static SearchNode goal;
	private class SearchNode
	{
		Board current;
		int moves;
		SearchNode prev;
		
		SearchNode(Board initial)
		{
			current = initial;
			prev=null;
			moves=0;
		}
	}
	
	public Solver(Board initial)
	{
		PriorityOrder po = new PriorityOrder();
		PriorityQueue <SearchNode>pq = new PriorityQueue<SearchNode>(po);
		int counter=0;
		SearchNode node = new SearchNode(initial);
		pq.add(node);
		SearchNode min = pq.remove();
		while(!min.current.isGoal())
		{
			if(counter++==1500)
			{
				System.out.println("Taking long time! Solution not possible!");
				System.exit(0);
			}
			for(Board b: min.current.neighbours())
			{
				if(min.prev==null || !b.equals(min.prev.current))
				{
					SearchNode n = new SearchNode(b);
					n.prev = min;
					n.moves=min.moves+1;
					pq.add(n);
				}
			}
			min = pq.remove();
		}
		
		if(min.current.isGoal())
		{
			goal = min;
		}
		else
		{
			goal =null;
		}
	}
	
	public boolean isSolvable()
	{
		return goal!=null;
	}
	
	public int noofmoves()
	{
		if(isSolvable())
		{
			return goal.moves;
		}
		else
		{
			return -1;
		}
	}
	public void printsteps(SearchNode result)
	{
		Stack<SearchNode> stk = new Stack<SearchNode>();
		
		while(result!=null)
		{
			stk.push(result);
			result = result.prev;
		}
		
		while(!stk.isEmpty())
		{
			printmatrix(stk.peek().current);
			stk.pop();
		}
	}
	
	public void printmatrix(Board board)
	{
		for(int i=0;i<board.N*board.N;i++)
		{
			if(i%3==0)
			{
				System.out.println();
			}
			System.out.print(board.board[i]+" ");
		}
		
		System.out.println("\n----------------");
	}
	
	public class PriorityOrder implements Comparator<SearchNode>
	{
		@Override
		public int compare(SearchNode n1, SearchNode n2)
		{
			int ma,mb;
			ma = n1.current.manhatton() + n1.moves;
			mb = n2.current.manhatton() + n2.moves;
			if(ma>mb) return 1;
			if(ma<mb) return -1;
			else return 0;
		}
	}
	
	public static void main(String args[])
	{
		int input[][] = new int[3][3];
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter elements of matrix");
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				input[i][j]= obj.nextInt();
			}
		}

		Board initial = new Board(input);
		Solver s = new Solver(initial);
		
		if(!s.isSolvable())
		{
			System.out.println("Can't be solved!");
		}
		else
		{
			System.out.println("No. of Steps: "+s.noofmoves());
			s.printsteps(goal);
		}
	}
}
