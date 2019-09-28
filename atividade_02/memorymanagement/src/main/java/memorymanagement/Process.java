package memorymanagement;

import java.util.List;


public class Process {
	
	private int size;
	private List<Page> pages;
	
	
	public int getSize() {
		return size;
	}
	
	public void setSize(int size) {
		this.size = size;
	}
	
	public List<Page> getPages() {
		return pages;
	}
	
	public void setPages(List<Page> pages) {
		this.pages = pages;
	}

}
