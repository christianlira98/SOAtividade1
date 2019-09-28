package memorymanagement;


public class Page {
	
	/**
	 * Page size in bytes
	 */
	public static final int SIZE = 4096;
	
	private int address;
	
	
	public int getAddress() {
		return address;
	}
	
	public void setAddress(int address) {
		this.address = address;
	}
	
}
