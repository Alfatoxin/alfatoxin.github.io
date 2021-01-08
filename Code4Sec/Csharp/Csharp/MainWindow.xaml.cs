using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using DataJuggler.Net5.Cryptography;

namespace Csharp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void btn_encrypt_Click(object sender, RoutedEventArgs e)
        {
            txt_encryptedresult.Text = CryptographyHelper.EncryptString(txt_plaintext.Text, txt_salt1.Text);
        }

        private void btn_decrypt_Click(object sender, RoutedEventArgs e)
        {
            txt_plaintextdecrypt.Text = CryptographyHelper.DecryptString(txt_encryptedtext.Text, txt_salt2.Text);
        }
    }
}
