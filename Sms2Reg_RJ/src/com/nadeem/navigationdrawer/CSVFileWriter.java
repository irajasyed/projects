package com.nadeem.navigationdrawer;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

import java.text.Format;
import java.awt.font.*;
public class CSVFileWriter {

private PrintWriter csvWriter,csvWriter1;    
File file;
public int flagma=0;

public CSVFileWriter(File file) {
    this.file = file;

}

public void writeHeader(String data) {
	
    try {
        if (data != null) {
            
            csvWriter = new PrintWriter(new FileWriter(file, true));
            if(flagma!=0)
            csvWriter.print(",");
            flagma=flagma+1;
            csvWriter.print(data.toUpperCase());
            
            
            csvWriter.close();

        }
      
    } catch (IOException e) {
        e.printStackTrace();
    }

}
public void nextLine()
{
	try
	{
	csvWriter1 = new PrintWriter(new FileWriter(file, true));
	csvWriter1.print("\n");
	csvWriter1.close();
	}
	catch(IOException e)
	{
		e.printStackTrace();
	}
}
}