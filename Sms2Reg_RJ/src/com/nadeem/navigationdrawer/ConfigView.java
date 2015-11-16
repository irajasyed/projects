package com.nadeem.navigationdrawer;

import java.io.File;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class ConfigView extends Activity
{
	private Button confButt,viewButt;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_addview);
		Bundle bb=getIntent().getExtras();
		final String evt=bb.getString("addview");
		Toast.makeText(getApplicationContext(), evt,Toast.LENGTH_SHORT).show();
		confButt=(Button)findViewById(R.id.button1);
		viewButt=(Button)findViewById(R.id.button2);
		confButt.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Intent i=new Intent(ConfigView.this,Header_add.class);
				i.putExtra("evt_name",evt);
				startActivity(i);
				
			}
		});
		viewButt.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
//				File videoFile2Play = new File("/sdcard/app1.csv");
				File videoFile2Play = new File("/sdcard/"+evt+".csv");
				Intent i = new Intent();
				i.setAction(android.content.Intent.ACTION_VIEW);
				i.setDataAndType(Uri.fromFile(videoFile2Play), "text/csv");
				startActivity(i);
				
				
			}
		});
				
}
}