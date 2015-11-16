package com.nadeem.navigationdrawer;

import java.util.ArrayList;
import java.util.HashMap;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class LazyAdapter extends BaseAdapter {

	private final Activity activity;
	private final ArrayList<HashMap<String, String>> data;
	private static LayoutInflater inflater=null;

	public LazyAdapter(Activity a, ArrayList<HashMap<String, String>> d) {
		activity = a;
		data=d;
		inflater = (LayoutInflater)activity.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
	}

	@Override
	public int getCount() {
		return data.size();
	}

	@Override
	public Object getItem(int position) {
		return position;
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		View vi=convertView;
		if(convertView==null)
			vi = inflater.inflate(R.layout.list_row, null);

		TextView title = (TextView)vi.findViewById(R.id.title); // title
//		TextView artist = (TextView)vi.findViewById(R.id.artist); // artist name
//		TextView duration = (TextView)vi.findViewById(R.id.duration); // duration

		HashMap<String, String> song = new HashMap<String, String>();
		song = data.get(position);

		// Setting all values in listview
		title.setText(song.get(SecondActivity.KEY_TITLE));
//		artist.setText(song.get(SecondActivity.KEY_ARTIST));
//		duration.setText(song.get(SecondActivity.KEY_DURATION));
		return vi;
	}
}