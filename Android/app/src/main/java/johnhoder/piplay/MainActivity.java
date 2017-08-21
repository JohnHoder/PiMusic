package johnhoder.piplay;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.Properties;
import java.util.UUID;

public class MainActivity extends Activity {
    private static final UUID PEBBLE_APP_UUID = UUID.fromString("01d5f030-6646-4d3b-a35f-0b2ff845f1d5");
    protected static final int RESULT_SPEECH = 1;
    Button btnSpeak;
    TextView txtText;
    Button sendBtn;
    EditText usr_nm;
    Button stop;


    String songname = "";
    public boolean isCancel = false;

    protected void onActivityResult(int paramInt1, int paramInt2, Intent paramIntent) {
        super.onActivityResult(paramInt1, paramInt2, paramIntent);

        String str1 = (String) paramIntent.getStringArrayListExtra("android.speech.extra.RESULTS").get(0);
        this.txtText.setText(str1);
        this.usr_nm.setText(str1);
    }

    protected void onCreate(Bundle paramBundle) {
        super.onCreate(paramBundle);
        setContentView(R.layout.activity_main);
        this.txtText = ((TextView) findViewById(R.id.lelid));
        this.txtText.setText("Hello, World!");
        this.btnSpeak = ((Button) findViewById(R.id.button));
        sendBtn = (Button) findViewById(R.id.sendBtn);
        usr_nm = (EditText) findViewById(R.id.editText1);
        stop = (Button) findViewById(R.id.stopBtn);

        //new initializeSSH().execute();

        //BUTTONS
        this.btnSpeak.setOnClickListener(new View.OnClickListener() {
            public void onClick(View paramAnonymousView) {
                startSTT();
            }
        });
        sendBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //String host = "x.x.x.x";
                songname = usr_nm.getText().toString();
                new loadsomestuff().execute(songname);
            }
        });
        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                isCancel = true;
                //new stopExecutionSSH().execute();
            }
        });

        Bundle extras = getIntent().getExtras();
        String value1 = extras.getString(Intent.EXTRA_TEXT);
        if(!value1.isEmpty()) {

            Toast.makeText(getApplicationContext(), value1, Toast.LENGTH_SHORT).show();
        }
    }

    void startSTT() {
        Intent localIntent = new Intent("android.speech.action.RECOGNIZE_SPEECH");
        localIntent.putExtra("android.speech.extra.LANGUAGE_MODEL", "en-US");
        try {
            startActivityForResult(localIntent, 1);
            this.txtText.setText("");
            this.usr_nm.setText("");
        } catch (ActivityNotFoundException localActivityNotFoundException) {
            Toast.makeText(getApplicationContext(), "Opps! Your device doesn't support Speech to Text", Toast.LENGTH_SHORT).show();
        }
    }

    public class loadsomestuff extends AsyncTask<String, Integer, String> {

        String asd;

        @Override
        protected String doInBackground(String... arg0) {

            JSch jsch = new JSch();

            Session session;

            Properties props = new Properties();
            props.put("StrictHostKeyChecking", "no");

            Properties config = new Properties();
            config.put("StrictHostKeyChecking", "no");
            config.put("compression.s2c", "zlib,none");
            config.put("compression.c2s", "zlib,none");

            try {
                session = jsch.getSession(Constants.USERNAME, Constants.ADDRESS, Constants.PORT);
                session.setConfig(config);
                session.setPassword(Constants.PASSWORD);
                session.connect();
            } catch (JSchException e) {
                asd = "NOT_Executed";
                System.out.println("NOT_executed");
                e.printStackTrace();
                return "NOT_Executed";
            }

            try {

                ChannelExec channel = (ChannelExec) session.openChannel("exec");
                channel.setPty(true);
                channel.setErrStream(System.err);
                OutputStream out = channel.getOutputStream();
                BufferedReader in = new BufferedReader(new InputStreamReader(channel.getInputStream()));
                channel.setCommand("pwd; cd /home/sonstiges/PiMusic/; python music_fm.py '" + arg0[0] + "'");
                channel.connect();
                String msg = null;
                while (true) {
                    //msg = in.readLine();
                    //System.out.println("inside loop - " + isCancel);
                    //System.out.println(msg + isCancel + "\n");
                    if (isCancel == true) {
                        break;
                    }
                }

                out.write(3);
                out.flush();

                channel.disconnect();
                session.disconnect();
            } catch (Exception e) {
                asd = "NOT_Executed";
                System.out.println("NOT_executed");
                e.printStackTrace();
                return "NOT_Executed";
            }

            System.out.println("executed");
            asd = "executed";
            isCancel = false;
            return "Executed";
        }

        @Override
        protected void onPostExecute(String abc) {
            txtText.setText(asd);
        }

    }
}