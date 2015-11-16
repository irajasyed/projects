package com.nadeem.navigationdrawer;



import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import android.content.Context;
import android.content.Intent;
import android.content.res.TypedArray;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ExpandableListView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.AdapterView.OnItemClickListener;

public class SecondActivity extends BaseActivity {
	private String[] navMenuTitles;
	private TypedArray navMenuIcons;
	ListView list;
	LazyAdapter adapter;
	FirstActivity fa=new FirstActivity();
	Context context=null;
	ArrayList<String> a1_backup=new ArrayList<String>();
	ArrayList<String> al = new ArrayList<String>();
	  
//	
//	static final String KEY_SONG = "song"; // parent node
//	static final String KEY_ID = "id";
	static final String KEY_TITLE = "title";
//	static final String KEY_ARTIST = "artist";
//	static final String KEY_DURATION = "duration";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_second);
		Bundle b=getIntent().getExtras();
//		if(b!=null)
//		{
			 a1_backup=(ArrayList<String>) ReadArrayListFromSD(getApplicationContext(),"eventlist");
					 
			 al=(ArrayList<String>) b.getStringArrayList("arrlist");
//		}
		navMenuTitles = getResources().getStringArray(R.array.nav_drawer_items); // load
		// titles
		// from
		// strings.xml

		navMenuIcons = getResources()
				.obtainTypedArray(R.array.nav_drawer_icons);// load icons from
		// strings.xml

		set(navMenuTitles, navMenuIcons);
ArrayList<HashMap<String, String>> categoriesList = new ArrayList<HashMap<String, String>>();
//String limit=String.valueOf(fa.evtArrayList.size());
//Integer s=fa.myarr.length;
//al=fa.evtArrayList;
		for(int i=0;i<a1_backup.size();i++) {
//			String mm=String.valueOf(al.size());
//			Toast.makeText(getApplicationContext(),mm,10).show();
		   
			HashMap<String, String> map = new HashMap<String, String>();
//			map.put(KEY_ID, St);
			//map.put(KEY_TITLE, "hello");
			String auc=a1_backup.get(i);
			map.put(KEY_TITLE,auc);
//			map.put(KEY_ARTIST, "raja");
//			map.put(KEY_DURATION, "100");
			categoriesList.add(map);

		}


		list=(ListView)findViewById(R.id.lview);

		// Getting adapter by passing xml data ArrayList
		adapter=new LazyAdapter(this, categoriesList);
		list.setAdapter(adapter);

		// Click event for single list row
		list.setOnItemClickListener(new OnItemClickListener() {
			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
//				String ss=parent.
				String aucd=a1_backup.get(position);
//				Toast.makeText(getApplicationContext(),"Item " +aucd+ " was clicked",10).show();
				Intent ip=new Intent(SecondActivity.this,ConfigView.class);
				ip.putExtra("addview", aucd);
				startActivity(ip);
			}

		});
    }
	public static Object ReadArrayListFromSD(Context mContext,String filename){
        try {
            FileInputStream fis = mContext.openFileInput(filename + ".dat");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Object obj= (Object) ois.readObject();
            fis.close();
            return obj;

        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<Object>();
        }
    }
    
	
}
