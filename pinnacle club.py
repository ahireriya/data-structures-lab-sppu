#include <iostream>
using namespace std;

class sll
{
    private:
    struct node
    {
        string name;
        int PRN;
        node *next;
    }*start;

    public:
    sll()
    {
        start=NULL;
    }
    void create();
    void display();
    void insert_begin();
    void insert_end();
    void insert_pos();
    void del_begin();
    void del_end();
    void del_pos();
    void count();
    void concatenate(sll obj2);
};

void sll::create()
{
    node *temp, *curr;
    int ans;
    do
    {
        temp=new node;
        temp->next=NULL;
        cout<<"Enter Name : ";
        cin>>temp->name;
        cout<<"Enter PRN : ";
        cin>>temp->PRN;
        if(start==NULL)
        {
            start=temp;
            curr=temp;
        }
        else
        {
            curr->next=temp;
            curr=curr->next;
        }
        cout<<"To add more press 1"<<endl;
        cin>>ans;
    }while(ans==1);
}

void sll::display()
{
    node *t;
    t=start;
    if(start==NULL)
    {
        cout<<"List is Empty"<<endl;
    }
    else
    {
        while(t!=NULL)
        {
            cout<<"Name : "<<t->name<<"; PRN : "<<t->PRN<<" --> ";
            t=t->next;
        }
        cout<<"NULL"<<endl;
    }
}

void sll::insert_begin()
{
    node *temp;
    temp=new node;
    temp->next=NULL;
    cout<<"Enter Name : ";
    cin>>temp->name;
    cout<<"Enter PRN : ";
    cin>>temp->PRN;
    temp->next=start;
    start=temp;
}

void sll::insert_end()
{
    node *temp;
    temp=new node;
    temp->next=NULL;
    cout<<"Enter Name : ";
    cin>>temp->name;
    cout<<"Enter PRN : ";
    cin>>temp->PRN;
    node *t=start;
    while(t->next!=NULL)
    {
        t=t->next;
    }
    t->next=temp;
}

void sll::insert_pos()
{
    node *temp;
    node *t=start;
    temp=new node;
    temp->next=NULL;
    cout<<"Enter Name : ";
    cin>>temp->name;
    cout<<"Enter PRN : ";
    cin>>temp->PRN;
    int pos;
    cout<<"Enter the position to insert node : ";
    cin>>pos;
    for (int i=1; i<pos-1; i++)
    {
        t=t->next;
    }
    temp->next=t->next;
    t->next=temp;
}

void sll::del_begin()
{
    node *t=start;
    start=start->next;
    cout<<t->name<<"'s has been deleted"<<endl;
    delete t;
}

void sll::del_end()
{
    node *t=start;
    node *back=start;
    while(t->next!=NULL)
    {
        back=t;
        t=t->next;
    }
    back->next=NULL;
    cout<<t->name<<"'s has been deleted"<<endl;
    delete t;
}

void sll::del_pos()
{
    node *t=start;
    node *back=start;
    int pos;
    cout<<"Enter the position to delete node : ";
    cin>>pos;
    for(int i=1; i<=pos-1; i++)
    {
        back=t;
        t=t->next;
    }
    back->next=t->next;
    cout<<t->name<<"'s has been deleted"<<endl;
    delete t;
}

void sll::count()
{
    node *t=start;
    int count=0;
    while(t!=NULL)
    {
        count++;
        t=t->next;
    }
    cout<<"Total Members : "<<count<<endl;
}

void sll::concatenate(sll obj2)
{
    node *t=start;
    while(t->next!=NULL)
    {
        t=t->next;
    }
    t->next=obj2.start;
    display();
}

int main()
{
    sll obj1, obj2;
    int ch;
    do
    {
        cout<<"\n1 : Create list";
        cout<<"\n2 : Display";
        cout<<"\n3 : Insert at Beginning";
        cout<<"\n4 : Insert at End";
        cout<<"\n5 : Insert at Position";
        cout<<"\n6 : Delete from Beginning";
        cout<<"\n7 : Delete from End";
        cout<<"\n8 : Delete from Position";
        cout<<"\n9 : Count Total Members";
        cout<<"\n10 : Concatenate two list";
        cout<<"\n11 : Exit";
        cout<<"\nEnter your Choice : ";
        cin>>ch;
        switch(ch)
        {
            case 1:
                obj1.create();
                break;
            case 2:
                obj1.display();
                break;
            case 3:
                obj1.insert_begin();
                break;
            case 4:
                obj1.insert_end();
                break;
            case 5:
                obj1.insert_pos();
                break;
            case 6:
                obj1.del_begin();
                break;
            case 7:
                obj1.del_end();
                break;
            case 8:
                obj1.del_pos();
                break;
            case 9:
                obj1.count();
                break;
            case 10:
                obj2.create();
                obj1.display();
                obj2.display();
                obj1.concatenate(obj2);
                break;
            case 11:
                cout<<"End of Program"<<endl;
                exit(0);
        }
    }while(ch!=11);
    return 0;
}
