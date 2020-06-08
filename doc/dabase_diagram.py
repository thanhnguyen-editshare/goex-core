'''
user <collection>
{
    _id: <objectid>
    username: <string>
    password: <md5>
    email: <string>
    phone: <list[string]>
    avatar: <string>
    visited: 
        place: <list[object]> [
            {
                place_id:<objectid>
                visite_date:<datetime>
            }
        ]
    album: <list[object]> {
        {
            album_id: <objectid>
            name: <string>
            create_date: <datetime>
            description: <string>
            photo: <list[object]>
            {
                photo_id: <objectid>
                name: <string>
                description: <string>
                href: <string>
            }
        }
    }
    //// we store it in redis
    location: <object> {
        long:<double>
        lat:<double>
    }
    ////
    region: <object>{
        country: <string>
    }    
    status: <object> {
        enable: <string>
        gps: <tring>
    }
    role: <objectid>
}

///we use elastic search to sync data article
article <colection>
{
    _id:<objectid>
    author:<objectid>
    topic:{
        type:string,
        id:<objectid>
    }
    header:<string>
    body:<string>
    rate: <list[object]>{
        rank:<int>
        user_id:<objectid>
    }
    comment: <list[object]>{
        comment:<list[object]>{..}
        content: <string>
        user_id:<objectid>  
    }
}

//// follow data standard global
country <collection>
{    
}

region <collection>
{
}

place <collection>
{
}
///////

group <collection> (comming soon)
{

}

role <collection> (comming soon)
{

}
'''