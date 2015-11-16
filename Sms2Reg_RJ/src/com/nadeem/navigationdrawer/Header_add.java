package com.nadeem.navigationdrawer;

//import com.android.R;

import java.io.File;
import java.util.ArrayList;

//import com.example.dynamiclistviewexample.R;






import com.nadeem.navigationdrawer.CSVFileWriter;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

public class Header_add extends Activity
{
	CSVFileWriter csv;
	StringBuffer filePath;
	File file;
	ImageView add_icn;
	Button b1;
	EditText headr;
	ListView headerlist;
//	private ArrayList<String> strArr;
	private ArrayAdapter<String> adapter;
//	MyApplication myA=new MyApplication();
	
	public void onCreate(Bundle savedInstanceState)
	{ 
		setContentView(R.layout.configure);
		b1=(Button)findViewById(R.id.button1);
		super.onCreate(savedInstanceState);
		Bundle bb1=getIntent().getExtras();
		final String evt=bb1.getString("evt_name");
		
		add_icn=(ImageView)findViewById(R.id.imageView1);
		headr=(EditText)findViewById(R.id.editText1);
		headerlist = (ListView) findViewById(R.id.listView1);
//		strArr = new ArrayList<String>();
//		for (int i = 0; i < 2; i++) {
//			strArr.add("Row:" + i);
//		}
		 filePath = new StringBuffer();
		    filePath.append("/sdcard/"+evt+".csv");
		    file = new File(filePath.toString());

		    csv = new CSVFileWriter(file);
		    
		adapter = new ArrayAdapter<String>(getApplicationContext(),
				android.R.layout.simple_list_item_1,MyApplication.strArr);
		headerlist.setAdapter(adapter);
		add_icn.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				MyApplication.strArr.add(headr.getText().toString());
				adapter.notifyDataSetChanged();
				
				csv.writeHeader(headr.getText().toString());
				headr.setText("");

			}
		});
		b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				csv.nextLine();
				
			}
		});
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}