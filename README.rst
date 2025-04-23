===========
PoS Order Invoice Wizard
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| |badge3| 

This module extends the functionality of the Point of Sale module to support invoicing PoS orders with a custom journal through a wizard, allowing you to invoice orders in 'paid' state even after the PoS session is closed.

**Table of contents**

.. contents::
   :local:

Install
=======

To install this module, you need to:

1. Clone or download the module into your Odoo addons directory.
2. Update the module list in Odoo (Apps > Update Apps List).
3. Search for "PoS Order Invoice Wizard" and click "Install".

Usage
=====

1. Go to **Point of Sale > Orders**.
2. Select one or more PoS orders in the 'paid' state.
3. Click on the action button "Facturar (Diario Personalizado)".
4. In the wizard, select the journal you want to use for invoicing.
5. Click "Facturar" to generate the invoices with the selected journal.
6. The system will open the newly created invoice for the first selected order.

Known issues / Roadmap
======================

* Currently, the wizard does not display a summary of the selected orders before invoicing. This feature may be added in future versions.

Bug Tracker
===========

For issues, feature requests, or support, please contact us at:

* Help Contact: `Be OnlyOne <https://onlyone.odoo.com/>`_

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne <https://onlyone.odoo.com/>`_

  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne.