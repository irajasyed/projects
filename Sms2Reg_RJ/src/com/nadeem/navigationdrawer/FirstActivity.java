package com.nadeem.navigationdrawer;



import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import android.app.Dialog;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.res.TypedArray;
import android.os.Bundle;
import android.support.v4.app.NotificationCompat;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

public class FirstActivity extends BaseActivity {
	private String[] navMenuTitles;
	private TypedArray navMenuIcons;
    private ImageView iv;
    private Context context = this;
    public Object[] myarr;
    Button view_eve;
  
//    public ArrayList<String> evtArrayList = new ArrayList<String>();
   
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		NotificationCompat.Builder mBuilder =
                new NotificationCompat.Builder(this)

               .setSmallIcon(R.drawable.evt)

               .setContentTitle("My title")

               .setOngoing(true)  

               .setContentText("Small text with details");
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_first);
		view_eve=(Button)findViewById(R.id.button1);
		
		
		view_eve.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Intent i=new Intent(FirstActivity.this,SecondActivity.class);
				i.putStringArrayListExtra("arrlist",evtArrayList);
				startActivity(i);
				
			}
		});
		navMenuTitles = getResources().getStringArray(R.array.nav_drawer_items); // load
																					// titles
																					// from
																					// strings.xml

		navMenuIcons = getResources()
				.obtainTypedArray(R.array.nav_drawer_icons);// load icons from
															// strings.xml

		set(navMenuTitles, navMenuIcons);
		iv=(ImageView)findViewById(R.id.imageView1);
		iv.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				// TODO Auto-generated method stub
				final Dialog dialog = new Dialog(context);
				dialog.setContentView(R.layout.alert);
				dialog.setTitle("Title!");
				final EditText et=(EditText)dialog.findViewById(R.id.editText11);
				Button btOK = (Button) dialog.findViewById(R.id.button11);
				btOK.setOnClickListener(new OnClickListener() {
					
					@Override
					public void onClick(View v) {
						// TODO Auto-generated method stub
						evtArrayList.add(et.getText().toString());
						SaveArrayListToSD(getApplicationContext(),"eventlist",evtArrayList);
						dialog.dismiss();
//					    Toast.makeText(getApplicationContext(),evtArrayList.get(0),10).show();
						
					}
				});
				dialog.show();
				
			
				
				
			}
		});
		
		
		
	}
	public static <E> void SaveArrayListToSD(Context mContext, String filename, ArrayList<E> evtArrayList)
	{
        try 
        {

            FileOutputStream fos = mContext.openFileOutput(filename + ".dat", mContext.MODE_PRIVATE);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(evtArrayList);
            fos.close();
        } 
        catch (Exception e) 
        {
            e.printStackTrace();
        }
    }
	  public void startService(View view) {
	      startService(new Intent(getBaseContext(), MyService.class));
	   }
	 
	   // Method to stop the service
//	   public void stopService(View view) {
//	      stopService(new Intent(getBaseContext(), MyService.class));
//	   }
	
}
