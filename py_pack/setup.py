from setuptools import find_packages, setup

package_name = 'py_pack'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/demo.launch.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='soliman',
    maintainer_email='ahmedsliman215@gmail.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publish = py_pack.takler:main",
            "subscribe = py_pack.listener:main",
            "client = py_pack.client_nod:main",
            "server = py_pack.server_nod:main",
            "moveRobo = py_pack.moverobot:main",
            "client_robot = py_pack.actionclient:main"
        ],
    },
    
)
