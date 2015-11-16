                   
            /*
             PROJECT NAME: JAVA IDE (BUJJU V1.0)
             DEVELOPERS  : RAJASYEDABUTHAHIR J,THIRUGNANASELVI.S
             DOMAIN      : JAVA

             */

         
             
             importjavax.swing.*;



             importjava.awt.*;

             importjava.awt.event.*;

             import java.io.*;

             public class editor extends JFrame implements ActionListener , KeyListener{ 

             JTextArea jta,jta1;

             JScrollPane jscroll;

             JButten nl ;

             JMenuBar mbar;

             JMenu file,edit,service,Developers;

             JMenuItem compile,run;

             JMenuItem fnew ,fexit, fopen, fsave;

             JMenuItem ecut ,ecopy, epaste, eselall, edel;

             JMeneItem rj,bj;

             String fname,fln;

             boolean chg;

             JPanel panel1,panel2;

             public editor()

             {

             setSize(1200,700);

             fname = "";

             chg = false;

             setLayout(new GridLayout(1,2));

             makemenu();

             setJMenuBar(mbar);

             panel1 =new JPanel();

             panel1.setSize(1200,300);

             panel1.setLayout(new BorderLayout());

             jta = new JTextArea();

             jta.setFont(new Font("Times New Romen",Font.PLAIN , 20) );

             jta.addKeyListener(this);

             jscroll = new JScrollPane(jta);

             n1 = new JButton("Workspace:");

             panel1.add(n1, BorderLayout.NORTH);

             panel1.add(jscroll, BorderLayout.CENTER);

             add(panel1);

             panel2=new JPanel();

             panel2.setLayout(new BorderLayout());

             JButten n2=new JButten("console:");

             panel2.add(n2, BorderLayout.NORTH);

             panel2.setSize(1200, 200);

             jta1=new JTextArea();

             jta1.setFont(new Font("Times New Romen",Font.PLAIN ,20) );

             JScrollPane jscroll1 = new JScrollPane(jta1);

             panel2.add(jscroll1,BorderLayout.CENTER);

             add(panel2);

             setVisible(true);

             setTitle("BUJJU-THE JAVA PROGRAMMING EDITOR v1.0 developed by Raja Syed Abuthahir&ThiruGnanaSelvi");

             setDefaultCloseOperation(EXIT_ON_CLOSE);

              }             

             ActionListener comp=new CompileListener();

             ActionListener runn=new RunListener();

             ActionListener abt=new AboutListener();

             
             public class AboutListener implements ActionListener

              {
             
             public void actionPerformed(ActionEvent ae)

             {

            JOptionPane.showMessageDialog(null,"Student at KPRIET\nROLL NO:64,94\nDept of CSE\n2012-2016 batch");

             }}
            
            public void ListenerPass(String fname,String fn)

            {

            String s1='"\'";

            String s2='"\'";

            fname=this.fname;

            fln = fn;

            fname.replace(s1,s2);

            n1.setText("Workspace : "+fln);

            }

            public class CompileListener implements ActionListener

            {

            public void actionPerformed(ActionEvent ae)

            {
    
            try{

            jta1.setText("");

            Process pro = Runtime().getRuntime().exec("javac "+fname);



            BufferedReader br=new BufferedReader(new InputStreemReader(pro.getErrorStream()));

            String err;

            if((err =br.readLine())==null)

            {

            jta1.append("Compiled Successfully");


            }    
       
            while((err= br.readLine()) !=null)

            {

            err=err+"\n";

            jta1.append(err);

          }}                  

            catch(Exception e)

            {}

            }}

            public  class RunListener implements ActionListener

            {

            public void actionPerformed(ActionEvent ae)

            {

            try{

            String er;

            jta1.setText("");

           fname=fname.replace(fln,"");

           fln=fln.replace(".java","");

           Process pro1 = Runtime.getRuntime().exec("java -cp "+fname+" "+fln);

           BufferedReader br1 =new BufferedReader(new InputStreamReader(pro1.getErrorStream()));

           while((er= br1.readLine()) !=null)

           {

           er=er+"\n";

           jta1.append(er);

          }

          BufferedReader br=newBufferedReader(new InputStreamReader(pro1.getInputStream()));

          String  opt;

          while((opt= br.readLine()) !=null)


          {
            
          opt=opt+"\n";

          jta1.append(opt);

          }}
          
          catch(Exception e)

          }}
         
          void makemenu()

          {

          mbar = new JMenuBar();

          file = new JMenu("File");

          edit = new JMenu("Edit");

          service=new JMenu("Service");

          Developers=newJMenu("DEVELOPERS");

          file.setMnemonic('F');

          edit.setMnemonic('E');

          fnew = newJMenuItem("New");

          fopen = new JMenuItem("Open");

          fsave = new JMenuItem("Save");

          fexit = new JMenu("Exit");

          eselall=new JMenuItem("Selectall");

          edel=new JMenuItem("Delete");

          compile=new JMenuItem("Compile");

          run=new JMenuItem("Run");

          rj=new JMenuItem("Raja Syed Abuthahir . J");

          bj=new JMenuItem('ThiruGnanaSelvi . S");

          file.add(fnew);

          file.add(fopen);

          file.add(fsave);





          file.addSeparator();

          file.add(fexit);

          edit.addSeparator();

          edit.add(eselall);

          edit.add(edel);

          service.add(compile);

          service.add(run);

          Developers.add(rj);

          Developers.add(bj);

          mbar.add(file);

          mbar.add(edit);

          mbar.add(service);

          mbar.add(Developers);

          fnew.addActionListener(this);

          fopen.addActionListener(this);

          fsave.addActionListener(this);

          fexit.addActionListener(this);

          eselall.addActionListener(this);

          edel.addActionListener(this);

          compile.addActionListener(comp);

          run.addActionListener(runn);

          rj.addActionListener(abt);

          bj.addActionListener(abt);

          KeyStroke k;

          k = KeyStroke.getKeyStroke('N', java.awt.Event.CTRL_MASK);

          fnew.setAccelerator(k);

          k = KeyStroke.getKeyStroke('O', java.awt.Event.CTRL_MASK);

          fopen.setAccelerator(k);





          k = KeyStroke.getKeyStroke('S', java.awt.Event.CTRL_MASK);

          fsave.setAccelerator(k);

          } public void keyPressed(KeyEvent e){}

           public void keyReleased(KeyEvent e){}

           public void keyTyped(KeyEvent e)

           {

           chg = true;

           }
          
            public void actionPerformed(ActionEvent e)
		{
             if(e.getSource().equals(eselall))

            {

            jta.selectAll();

            }
           else if(e.getSource().equals(fnew))
		{
      
            fname = "";

            chg = false;

            jta.setText(" ");

            }
	else if(e.getSource().equals(fopen))
            {

            fileopen();

            }
	else if(e.getSource().equals(fsave))
            {
           
            filesave();

            }
	else if(e.getSource().equals(fexit))
		{

            fileexit();

            }

            }
	   void fileexit()

            {

            if(chg == true)

           {

            int res;

            res = JOptionPane.showConfirmDialog(this, "Do You Want to Save Changes", "File Exit",JOptionPane.YES_NO_CANCEL_OPTION);

            if(res == JOptionPane.YES_OPTION)

            {

            filesave();

            }

            else if(res == JOptionPane.CANCEL_OPTION)

             {

           return;

           }}

          System.exit(0);

           }

          void fileopen()

         {

         JFileChooser jfc = new JFileChooser();

         jfc.setFileSelectionMode(jfc.FILES_ONLY);

        int res = jfc.showOpenDialog(this);



        if(res == jfc.APPROVE_OPTION)

        {File f = jfc.getSelectedFile();



       try

       {

      FileReader fr = new FileReader(f);

      BufferedReader br = new BufferedReader(fr);

      String data;

      jta.setText("");

      while( (data =br.readLine()) != null)

      {

      data = data + "\n";

      jta.append(data);

      }

     fname = f.getAbsolutePath();

     String fn=f.getName().toString();

     ListenerPass(fname,fn);

     br.close();

     fr.close();

     }

     catch(IOException e)

     {
    
     JOptionPane.showMessageDialog(this , e.getMessage() ,"File Open Error",JOptionPane.ERROR_MESSAGE);

     }}}

     void filesave()

     {

     if(fname.equals(""))

     {


    JFileChooser jfc = new JFileChooser();

    jfc.setFileSelectionMode(jfc.DIRECTORIES_ONLY);



    int res = jfc.showSaveDialog(this);

    if(res == jfc.APPROVE_OPTION)

    {

    File f = jfc.getSelectedFile();

    fname = f.getAbsolutePath();

    filewrite();

    }

    }

    else

    filewrite();

    }

    void filewrite()

    {

    try

    {

    FileWriter fw = new FileWriter(fname);

    fw.write(jta.getText());

   fw.flush();fw.close();

    chg = false;

   }catch(IOException e) {

   JOptionPane.showMessageDialog(this , e.getMessage() ,"File Save Error",JOptionPane.ERROR_MESSAGE);

   }
}

   public static void main(String args[])

   {
	new editor();
   }

    }





    



           


            

             


             

             