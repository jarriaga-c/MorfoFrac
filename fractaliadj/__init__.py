# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Fractalidad
                                 A QGIS plugin
 Estu pligin optiene las capas de fractalidad
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-05-27
        copyright            : (C) 2021 by Jair Arriaga, Tonatiuh Suarez
        email                : jair.arriaga@outlook.com, tonatiuhsmeaney@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Jair Arriaga, Tonatiuh Suarez'
__date__ = '2021-05-27'
__copyright__ = '(C) 2021 by Jair Arriaga, Tonatiuh Suarez'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Fractalidad class from file Fractalidad.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .FractaliadJ import FractalidadPlugin
    return FractalidadPlugin()
