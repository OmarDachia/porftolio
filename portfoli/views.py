from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """Home page with hero section"""
    context = {
        'name': 'John Developer',
        'title': 'Full Stack Developer',
        'tagline': 'Building amazing web experiences',
        'bio': 'I create beautiful, functional, and user-friendly websites and applications.',
        'cta_text': 'View My Work',
        'cta_link': '/projects/',
    }
    return render(request, 'home.html', context)

def about(request):
    """About page with skills and experience"""
    context = {
        'name': 'John Developer',
        'title': 'Full Stack Developer',
        'bio': """
            I'm a passionate developer with 5+ years of experience in web development.
            I love creating clean, efficient code and building applications that make a difference.
            When I'm not coding, I enjoy contributing to open-source projects and mentoring junior developers.
        """,
        'skills': {
            'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Vue.js'],
            'Backend': ['Python', 'Django', 'Flask', 'Node.js', 'PHP'],
            'Database': ['PostgreSQL', 'MySQL', 'MongoDB', 'SQLite'],
            'Tools': ['Git', 'Docker', 'AWS', 'VS Code', 'Figma'],
            'Other': ['REST APIs', 'GraphQL', 'CI/CD', 'Agile/Scrum']
        },
        'experience': [
            {
                'title': 'Senior Developer',
                'company': 'Tech Corp',
                'period': '2022 - Present',
                'description': 'Leading development team on enterprise projects'
            },
            {
                'title': 'Full Stack Developer',
                'company': 'Startup Inc',
                'period': '2020 - 2022',
                'description': 'Built and maintained web applications from scratch'
            },
            {
                'title': 'Junior Developer',
                'company': 'Web Agency',
                'period': '2019 - 2020',
                'description': 'Developed client websites and applications'
            }
        ],
        'education': {
            'degree': 'B.S. Computer Science',
            'institution': 'MIT University',
            'year': '2019'
        }
    }
    return render(request, 'about.html', context)

def projects(request):
    """Projects page with sample projects"""
    projects_list = [
        {
            'id': 1,
            'title': 'E-Commerce Platform',
            'description': 'A full-featured online store with payment processing, user authentication, and admin dashboard.',
            'technologies': ['Django', 'PostgreSQL', 'Bootstrap', 'Stripe API'],
            'image': '🛒',
            'category': 'Full Stack',
            'live_url': '#',
            'github_url': '#',
            'features': [
                'User authentication and profiles',
                'Product catalog with search',
                'Shopping cart and checkout',
                'Payment integration',
                'Admin dashboard',
                'Order tracking'
            ]
        },
        {
            'id': 2,
            'title': 'Task Management App',
            'description': 'A collaborative project management tool with real-time updates, team workspaces, and task tracking.',
            'technologies': ['React', 'Django REST', 'WebSocket', 'Redis'],
            'image': '📋',
            'category': 'Full Stack',
            'live_url': '#',
            'github_url': '#',
            'features': [
                'Real-time updates',
                'Team workspaces',
                'Task assignment',
                'Progress tracking',
                'File attachments',
                'Comment system'
            ]
        },
        {
            'id': 3,
            'title': 'Weather Dashboard',
            'description': 'Interactive weather application with live data, 7-day forecast, and location-based weather alerts.',
            'technologies': ['JavaScript', 'React', 'Weather API', 'CSS3'],
            'image': '🌤️',
            'category': 'Frontend',
            'live_url': '#',
            'github_url': '#',
            'features': [
                'Live weather data',
                '7-day forecast',
                'Location detection',
                'Weather alerts',
                'Interactive maps',
                'Responsive design'
            ]
        },
        {
            'id': 4,
            'title': 'Blog Platform',
            'description': 'A modern blogging platform with markdown support, categories, tags, and user comments.',
            'technologies': ['Django', 'Bootstrap', 'Markdown', 'SQLite'],
            'image': '📝',
            'category': 'Backend',
            'live_url': '#',
            'github_url': '#',
            'features': [
                'Markdown editor',
                'Categories and tags',
                'Comment system',
                'User profiles',
                'Search functionality',
                'RSS feed'
            ]
        }
    ]
    
    context = {
        'projects': projects_list,
        'total_projects': len(projects_list),
        'categories': ['All', 'Full Stack', 'Frontend', 'Backend']
    }
    return render(request, 'projects.html', context)

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        errors = {}
        
        # Validation
        if not name:
            errors['name'] = 'Name is required'
        elif len(name) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        
        if not email:
            errors['email'] = 'Email is required'
        elif '@' not in email or '.' not in email:
            errors['email'] = 'Please enter a valid email address'
        
        if not message:
            errors['message'] = 'Message is required'
        elif len(message) < 10:
            errors['message'] = 'Message must be at least 10 characters'
        
        if errors:
            context = {
                'form_data': request.POST,
                'errors': errors,
                'show_success': False
            }
            return render(request, 'contact.html', context)
        
        # Simulate sending email (in development, prints to console)
        try:
            full_message = f"""
            From: {name} ({email})
            Subject: {subject or 'No Subject'}
            
            Message:
            {message}
            """
            
            send_mail(
                subject=f"Portfolio Contact: {subject or 'New Message'}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@portfolio.com',
                recipient_list=['your-email@example.com'],
                fail_silently=False,
            )
        except Exception as e:
            # In production, log the error
            pass
        
        # Show success message
        context = {
            'show_success': True,
            'name': name,
            'email': email,
            'message_sent': True
        }
        return render(request, 'contact.html', context)
    
    # GET request
    context = {
        'form_data': {},
        'errors': {},
        'show_success': False
    }
    return render(request, 'contact.html', context)