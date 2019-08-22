#include<stdio.h>
#include<string.h>
#include<math.h>
void main(){
  int t;
  scanf("%d",&t);

  while(t!=0 && t<=100){
    int i,j,n;
    scanf("%d",&n );

    if(n<=100 && n!=0){

      char ch[n][20];

      for(i=0;i<n;i++){
        scanf("%s",ch[i]);
      }

      float c=0;

      for(i=0;i<n;i++){

        float ci=0.2;
        if(strcmp(ch[i],"w")==0){
          continue;
        }

        int w=0;
        if (ch[i][0] == 'd' || ch[i][0]=='f')
          w=1;
        else
          w=0;

        int l= strlen(ch[i]);

        for(j=1;j<l;j++){
          int h;
          if(ch[i][j] == 'd' || ch[i][j]=='f')
            h=1;
          else
            h=0;
          if (w==h)
            ci+=0.4;
          else
            ci+=0.2;
          w=h;
        }

        for(j=0;j<i;j++){
          if(strcmp(ch[i],ch[j])==0){
            ci=(ci/2.0);
            // strcpy(ch[j],"w");
            break;
          }
        }

        c+=ci;
      }

      c=c*10;
      int b=(int)c;
      printf("%d\n",b);

    }

    t--;
  }
}
