package com.nadeem.navigationdrawer;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.widget.Toast;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.*;
import android.util.Log;
import android.widget.Toast;
import au.com.bytecode.opencsv.*;
public class MyService extends Service {
   @Override
   public IBinder onBind(Intent arg0) {
      return null;
   }

   @Override
   public int onStartCommand(Intent intent, int flags, int startId) {
      // Let it continue running until it is stopped.
//      Toast.makeText(this, "Service Started", Toast.LENGTH_LONG).show();



      class Sms2regReceiver extends BroadcastReceiver {
           
          // Get the object of SmsManager
          final SmsManager sms = SmsManager.getDefault();
          public  ArrayList<String> evtlist =(ArrayList<String>) ReadArrayListFromSD(getApplicationContext(),"eventlist");
//        		  new ArrayList<String>();
          public Object ReadArrayListFromSD(Context mContext,String filename){
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
          public void onReceive(Context context, Intent intent) {
          
             
              final Bundle bundle = intent.getExtras();
       
              try {
                   
                  if (bundle != null) {
                       
                      final Object[] pdusInfo= (Object[]) bundle.get("pdus");
                       
                     for (int i = 0; i < pdusInfo.length; i++) {
                           
                          SmsMessage onMessage = SmsMessage.createFromPdu((byte[]) pdusInfo[i]);
                          String phoneNumber = onMessage.getDisplayOriginatingAddress();
                           
                          String senderNum = phoneNumber;
                          String message = onMessage.getDisplayMessageBody();
                          String[] ms=message.split(" ");
//                      	String[] s2=e.split("This ");
//                  		String[] s3=s2[1].split(" ");
                        
                   
                          
                           
       
                         // Show Alert
                          int duration = Toast.LENGTH_LONG;
//                          FirstActivity fa=new FirstActivity();
                          int no_of_event=evtlist.size();
                          for(int ii=0;ii<=no_of_event;ii++)
                          {
                          if(ms[0].equals(evtlist.get(ii)))
                          {
                          Toast toast = Toast.makeText(context,
                                       "1 partipant Added for the event "+evtlist.get(ii), duration);
                          toast.show();
                          
//                          mainActivity ma=new mainActivity();
                          
//                          File file=new File("/sdcard/appatho.csv");
//                          if(file.exists()){
                   	 	   try {
//                   	 		    
//                   	 		    CSVWriter writer = new CSVWriter(new FileWriter("/sdcard/appo.csv",true));
                   	 		  CSVWriter writer = new CSVWriter(new FileWriter("/sdcard/"+ms[0].toUpperCase()+".csv",true));
//                   	 		   
                   	 		    
//                   	 		    String record =ms[1];
                   	 		      //Write the record to file
//                   	 		      String ms2[]=ms.;
                   	 		  String[] my_msg=message.split(ms[0]+" ");
                   	 		  String[] my_args=my_msg[1].split(" ");
//                   	 		      writer.writeNext(ms);
                   	 		  writer.writeNext(my_args);
                   	 		        
                   	 		      //close the writer
                   	 		      writer.close();
                   	 		         } catch (IOException e) {
                   	 		    e.printStackTrace();
                   	 		   }
//                   	 		  }
                          String messageToSend = "Thank you for your registration!!!";
                          String number =senderNum;

                          SmsManager.getDefault().sendTextMessage(number, null, messageToSend, null,null);
//                          File f=new File("abc.txt");
                         
                          }
                          } //for loop end
                      } // end for loop
                    } // bundle is null
       
              } catch (Exception e) {
                  Log.e("SmsReceiver", "Exception smsReceiver" +e);
                   
              }
          }   }
      
      return START_STICKY;
   
   }
   @Override
   public void onDestroy() {
      super.onDestroy();
      Toast.makeText(this, "Service Destroyed", Toast.LENGTH_LONG).show();
   }
}