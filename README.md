<h1>PythonForNetworking_FinalAssignment</h1>

<h2>Description</h2>

This Python script is designed to perform simple encryption and decryption of text files using a symmetric key. The script provides command-line arguments to perform the following:
<ul>
  <li>Generate a secure key and save it to a text file.</li>
  <li>Encrypt a plain text message with the secure key and save the encrypted message to a file.</li>
  <li>Decrypt encrypted messages with the key and display the original text.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python</li>
  <li>cryptography library <code>pip install cryptography</code></li>
</ul>

<h2>Usage</h2>

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>--generateKey</td>
      <td>Generates a symmetric encryption key and saves it to the current directory as myKey.</td>
      <td>python noahsCryptoTool.py --generateKey</td>
    </tr>
    <tr>
      <td>--encrypt</td>
      <td>Path to the plain text message to encrypt. (Requires --key and --name arguments.)</td>
      <td>python noahsCryptoTool.py --encrypt message.txt --key myKey --name encrypted_message.txt</td>
    </tr>
    <tr>
      <td>--decrypt</td>
      <td>Path to the encrypted message to decrypt. (Requires --key.)</td>
      <td>python noahsCryptoTool.py --decrypt encrypted_message.txt --key myKey</td>
    </tr>
    <tr>
      <td>--key</td>
      <td>Path to the key file used for encryption or decryption.</td>
      <td>--key myKey</td>
    </tr>
    <tr>
      <td>--name</td>
      <td>Name of the encrypted message file.</td>
      <td>--name encrypted_message.txt</td>
    </tr>
  </tbody>
</table>
