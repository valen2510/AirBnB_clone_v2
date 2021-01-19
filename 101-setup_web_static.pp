# Set up server for deployment of static content
package {'nginx':
    ensure => 'present'
}
exec {'Setup_for_deployment':
    command  => 'sudo mkdir -p /data/web_static/releases/test/;
    sudo mkdir -p /data/web_static/shared/;
    sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html;
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
    sudo chown -R ubuntu:ubuntu /data/;
    sudo sed -i '57 i \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default;
    sudo service nginx restart',
    provider => 'shell',
}
