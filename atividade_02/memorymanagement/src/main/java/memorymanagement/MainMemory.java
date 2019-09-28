package memorymanagement;


public class MainMemory {
	
	private int memorySize;
	private Page[] memory;
	
	
	public MainMemory(int memorySize) {
		this.memorySize = memorySize;		
		int numberOfPages = this.memorySize / Page.SIZE;
		this.memory = new Page[numberOfPages];
	}
	
	
	public void displayMemory() {
		System.out.println("+--------------------+");
		
		for(int k = 0; k < memory.length; k = k + 100) {
			System.out.print("|                    |");
		}
		
		System.out.println("+--------------------+");
	}
	
	
}
