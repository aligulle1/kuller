#include  <stdio.h>
#include <iksemel.h>

static int tmp=0;
int pr_tag (void *udata, char *name, char **atts, int type)
{
    switch (type) {
        case IKS_OPEN:
         //   printf ("%s", name);
              if(strcmp(name,"Version")==0){
                // printf("*%s*", element);
                   tmp=1;
               }
              if(strcmp(name,"Name")==0){
                   tmp=1;
               }
              if(strcmp(name,"Size")==0){
                   tmp=1;
              }


            break;
        case IKS_CLOSE:
         //   printf ("</%s> ", name);
            break;
        case IKS_SINGLE:
         //   printf ("%s/>", name);
            break;
    }
    if(tmp==1){
    if (atts) {
        int i = 0;
        while (atts[i]) {
            printf ("%s=’%s’", atts[i], atts[i+1]);
            i += 2;
        }
    }
    }
    return IKS_OK;
}
enum ikserror pr_cdata (void *udata, char *data, size_t len)
{
    int i;
    if(tmp==1){
        for (i = 0; i < len; i++)
            putchar (data[i]);
        tmp=0;
        printf("\n");
    }
    
       return IKS_OK;
}
int main (int argc, char *argv[])
{
    char buffer[100000];
    FILE *dosya;
    char str[1000];
    dosya=fopen("surumler.xml","r");
    size_t file_size;
    int done;

    do{
        file_size = fread(buffer,sizeof(char),100000,dosya);
        dosya = file_size < sizeof(buffer);

         iksparser *p;
         p = iks_sax_new (NULL, pr_tag, pr_cdata);
         switch (iks_parse (p,buffer, 0, 1)) {
            case IKS_OK:
                puts ("OK");
                break;
            case IKS_NOMEM:
                puts ("Not enough memory");
                exit (1);
            case IKS_BADXML:
                 puts ("XML document is not well-formed");
                 exit (2);
            case IKS_HOOK:
                 puts ("Our hooks didn’t like something");
                 exit (2);
        }
        iks_parser_delete (p);
        return 0;
    }
    while(!done);
    fclose(dosya);
}
