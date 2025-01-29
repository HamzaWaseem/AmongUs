import React from 'react';
import { Grid, Card, CardContent, Typography, CardActionArea } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import {
    Cloud as CloudIcon,
    Security as SecurityIcon,
    Lock as LockIcon,
    Code as CodeIcon,
} from '@mui/icons-material';

const services = [{
        title: 'Cloud Security',
        description: 'Analyze and monitor cloud infrastructure security',
        icon: CloudIcon,
        path: '/cloud-security',
        color: '#1976d2',
    },
    {
        title: 'Compliance',
        description: 'Check compliance with security standards',
        icon: SecurityIcon,
        path: '/compliance',
        color: '#388e3c',
    },
    {
        title: 'Data Encryption',
        description: 'Verify data encryption and key management',
        icon: LockIcon,
        path: '/data-encryption',
        color: '#d32f2f',
    },
    {
        title: 'Dependency Management',
        description: 'Analyze and secure project dependencies',
        icon: CodeIcon,
        path: '/dependency-management',
        color: '#7b1fa2',
    },
];

function Dashboard() {
    const navigate = useNavigate();

    return ( <
        div >
        <
        Typography variant = "h4"
        gutterBottom >
        Security Audit Dashboard <
        /Typography> <
        Grid container spacing = { 3 } > {
            services.map((service) => {
                const Icon = service.icon;
                return ( <
                    Grid item xs = { 12 }
                    sm = { 6 }
                    md = { 3 }
                    key = { service.title } >
                    <
                    Card >
                    <
                    CardActionArea onClick = {
                        () => navigate(service.path)
                    } >
                    <
                    CardContent >
                    <
                    Icon sx = {
                        {
                            fontSize: 40,
                            color: service.color,
                            mb: 2,
                        }
                    }
                    /> <
                    Typography gutterBottom variant = "h5"
                    component = "div" > { service.title } <
                    /Typography> <
                    Typography variant = "body2"
                    color = "text.secondary" > { service.description } <
                    /Typography> < /
                    CardContent > <
                    /CardActionArea> < /
                    Card > <
                    /Grid>
                );
            })
        } <
        /Grid> < /
        div >
    );
}

export default Dashboard;