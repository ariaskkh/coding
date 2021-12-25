import React from 'react'
import { useParams } from 'react-router-dom';

const data = { // username은 Dean과 kangho
    Dean: {
        name: '김강호',
        description: '리액트를 좋아하는 개발자'
    },
    kangho: {
        name: '캉호우',
        description: '캉호우호우'
    }
};

const Profile = () => {
    // const { username } = match.params;
    const { username } = useParams();
    const profile = data[username];
    if (!profile) {
        return <div>존재하지 않는 사용자입니다.</div>;
    }
    return (
        <div>
            <h3>
                {username}({profile.name})
            </h3>
            <p>{profile.description}</p>
        </div>
    );
};

export default Profile;