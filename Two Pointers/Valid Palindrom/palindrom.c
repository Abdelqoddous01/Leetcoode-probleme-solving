#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool Isalpha(char c){
    if (c>='a' && c<='z'){return true;};
    if (c>='A' && c<='Z'){return true;};
    if (c>='0' && c<='9'){return true;};
    return false;
}

bool isPalindrome(char *s){

    int counter=0;

    for (int i= 0; i < strlen(s); i++)
    {
        if (Isalpha(s[i]))
        {
            counter++;
        }
    }


    char news[counter+1];

    int index=0;

    for (int i= 0; i < strlen(s); i++)
    {
        if (Isalpha(s[i]))
        {
            news[index]=tolower(s[i]);
            index++;
        }
    }

    news[index]='\0';

    int valid=1;

    if (strlen(news)==1 )
    {
        return false;
    }
    else if(strlen(news)==0){
        return true;
    }

    for (int i = 0; i<counter; i++)
    {
        if (news[i]!=news[counter-1-i])
        {
            valid=0;
            break;
        }

    }

    return valid;
}


int main(){
    char s[100]="0";

    int res=isPalindrome(s);
    printf("%d",res);

    return 0;
}