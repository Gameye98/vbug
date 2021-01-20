package sec.blackhole.fbids;

import android.app.*;
import android.os.*;
import android.widget.*;
import android.text.*;
import android.content.*;
import org.jsoup.nodes.*;
import org.jsoup.*;
import java.io.*;
import java.util.*;
import org.json.*;

public class MainActivity extends Activity 
{
	public void Scroll() {
		ScrollView tscroll = (ScrollView) findViewById(R.id.tscroll);
		tscroll.fullScroll(tscroll.FOCUS_DOWN);
	}
	public void saveData(String username) {
		try {
			FileOutputStream out = new FileOutputStream("/sdcard/FB_IDs/.username");
			out.write(username.getBytes());
			out.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	public String loadData() {
		try {
			Scanner sc = new Scanner(new File("/sdcard/FB_IDs/.username"), "UTF-8");
			sc.useDelimiter("$^");
			return sc.next();
		} catch(Exception e) {
			return null;
		}
	}
	public void inputToken(final String userid) {
		AlertDialog.Builder dia = new AlertDialog.Builder(MainActivity.this);
		dia.setMessage(Html.fromHtml("<b>FACEBOOK TOKEN</b>"));
		final EditText input = new EditText(this);
		input.setHint("EAAAAUa ...");
		dia.setView(input);
		dia.setPositiveButton("Confirm", new DialogInterface.OnClickListener() {
				public void onClick(DialogInterface dialog, int whichButton) {
					try {
						FileOutputStream out = new FileOutputStream("/sdcard/FB_IDs/token.log");
						out.write(input.getText().toString().getBytes());
						out.close();
						TextView xterm = (TextView) findViewById(R.id.xterm);
						xterm.append(Html.fromHtml("<br><font color='green'>[+]</font><font color='white'> Gathering ID from "+userid+"</font><br>"));
						new SendTask().execute(userid);
					} catch(Exception e) {
						e.printStackTrace();
					}
				}
			});
		dia.setNegativeButton("Cancel", null);
		dia.show();
	}
	public void collectId() {
		AlertDialog.Builder dlg = new AlertDialog.Builder(this);
		dlg.setMessage(Html.fromHtml("<b>Enter the username</b>"));
		final EditText input = new EditText(MainActivity.this);
		input.setHint("username");
		input.setSingleLine(true);
		dlg.setView(input);
		dlg.setPositiveButton("Confirm", new DialogInterface.OnClickListener() {
				public void onClick(DialogInterface dialog, int whichButton) {
					File cookie = new File("/sdcard/FB_IDs/token.log");
					if(cookie.exists() == true) {
						if(cookie.isFile() == true) {
							TextView xterm = (TextView) findViewById(R.id.xterm);
							String userid = input.getText().toString();
							saveData(userid);
							xterm.append(Html.fromHtml("<br><font color='green'>[+]</font><font color='white'> Gathering ID from "+userid+"</font><br>"));
							new SendTask().execute(userid);
						} else {
							cookie.delete();
							inputToken(input.getText().toString());
						}
					} else {
						inputToken(input.getText().toString());
					}
				}
			});
		dlg.setNegativeButton("Cancel", null);
		dlg.show();
	}
	private class SendTask extends AsyncTask<String, Void, String>
	{
		@Override
		protected String doInBackground(String[] params)
		{
			try {
				Scanner fbtoken = new Scanner(new File("/sdcard/FB_IDs/token.log"), "UTF-8");
				fbtoken.useDelimiter("$^");
				String content = Jsoup.connect("https://graph.facebook.com/"+params[0]+"/friends?access_token="+fbtoken.next()).get().text();
				return content;
			} catch(Exception e) {
				e.printStackTrace();
				return null;
			}
		}
		@Override
		protected void onPostExecute(String result)
		{
			if(result != null) {
				TextView xterm = (TextView) findViewById(R.id.xterm);
				String idlist = "";
				try {
					JSONObject obj = new JSONObject(result);
					JSONArray arr = new JSONArray(obj.getString("data"));
					for(int x = 0;x < arr.length();x++) {
						JSONObject uid = arr.getJSONObject(x);
						xterm.append(Html.fromHtml("<font color='yellow'>"+uid.getString("id")+"</font><br>"));
						idlist = idlist + uid.getString("id") + "\n";
						Scroll();
					}
					try {
						String username = loadData();
						if(username != null) {
							try {
								FileOutputStream out = new FileOutputStream("/sdcard/FB_IDs/"+username);
								out.write(idlist.getBytes());
								out.close();
							} catch(Exception e) {
								e.printStackTrace();
							}
						}
					} catch(Exception e) {

					}
				} catch(Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
		File token = new File("/sdcard/FB_IDs");
		if(token.exists() == true) {
			if(token.isFile() == true) {
				token.delete();
				token.mkdir();
			} else {
				//nothing to do
			}
		} else {
			token.mkdir();
		}
		File cookie = new File("/sdcard/FB_IDs/token.log");
		if(cookie.exists() == true) {
			if(cookie.isDirectory() == true) {
				cookie.delete();
			}
		}
		TextView xterm = (TextView) findViewById(R.id.xterm);
		xterm.append("################################################\n");
		xterm.append("#            Facebook IDs Gathering            #\n");
		xterm.append("#              BlackHole Security              #\n");
		xterm.append("#              19 - March - 2019               #\n");
		xterm.append("################################################\n");
    }
	@Override
	public void onBackPressed()
	{
		AlertDialog.Builder dlg = new AlertDialog.Builder(MainActivity.this);
		dlg.setTitle("FB_IDs");
		dlg.setMessage("You can gather ids from someone friendlist with ease.\nThis app does ids gathering for you and does not require root, sometimes the best way to get good collection of ids is to make friends with someone you want the friendlist ids to be gathered.\nThe result will be saved in the /sdcard/FB_IDs.\n\nCopyright (C) 2019 by DedSecTL\n\nDedSecTL\nCvar1984\nCiKu370\nMr.TenSwapper07\namsitlab\n[M]izuno\n3RROR_TMX\nMr.K3N\nZetSec\nTroublemaker97\nL_Viole\nX14N23N6\nMR.R45K1N\nlord.zephyrus\n4cliba788\nmr0x100\nMrx04\nViruz\nMr_007\nIdannovita.\nBlackHole Security.");
		dlg.setPositiveButton("Gather", new DialogInterface.OnClickListener() {
				public void onClick(DialogInterface dialog, int whichButton) {
					collectId();
				}
			});
		dlg.setNeutralButton("Contact", new DialogInterface.OnClickListener() {
				public void onClick(DialogInterface dialog, int whichButton) {
					new AlertDialog.Builder(MainActivity.this)
						.setMessage("Instagram : @dtlily\nTelegram : @dtlily\nGitHub : Gameye98\nGitLab : dtlily")
						.show();
				}
			});
		dlg.setNegativeButton("Exit", new DialogInterface.OnClickListener() {
				public void onClick(DialogInterface dialog, int whichButton) {
					finish();
				}
			});
		dlg.show();
	}
}
