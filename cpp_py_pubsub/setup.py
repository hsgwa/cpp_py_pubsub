from setuptools import setup
import glob
import os

package_name = 'cpp_py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
		('share/cpp_py_pubsub/launch',
		 glob.glob(os.path.join('launch', '*.launch.py'))),

    ],
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='hasegawa',
    maintainer_email='hasegawa@isp.co.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
