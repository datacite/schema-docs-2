resourceTypeGeneral
=====================================

*Used by:*

* :ref:`10.a`
* :ref:`12.f`
* :ref:`20.a`

*Options:* [#f1]_

.. contents:: :local:
    :backlinks: none


.. _Audiovisual:

Audiovisual
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A series of visual representations imparting an impression of motion when shown in succession. May or may not include sound.

**Examples and Usage Notes:** May be used for films, video, etc.

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.17608/k6.auckland.4620790.v1

**Suggested Dublin Core Mapping:** MovingImage


.. _Award:

Award
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An umbrella term for resources provided to individual(s) or organization(s) in support of research, academic output, or training, such as a specific instance of funding, grant, investment, sponsorship, scholarship, recognition, or non-monetary materials.

**Examples and Usage Notes:** 

.. code:: xml

  <resourceType resourceTypeGeneral="Award">Grant</resourceType>

.. code:: xml

  <resourceType resourceTypeGeneral="Award">Facility use</resourceType>

**Suggested Dublin Core Mapping:** N/A


.. _Book:

Book
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Book">Textbook</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _BookChapter:

BookChapter
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** One of the main divisions of a book.

**Examples and Usage Notes:**

https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.15122/isbn.978-2-406-09313-8.p.0639

https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.17613/m6631d

**Suggested Dublin Core Mapping:** Text


.. _Collection:

Collection
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An aggregation of resources, which may encompass collections of one resourceType as well as those of mixed types. A collection is described as a group; its parts may also be separately described.

**Examples and Usage Notes:** A collection of samples, or various files making up a report

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.1594/pangaea.877589

**Suggested Dublin Core Mapping:** Collection


.. _ComputationalNotebook:

ComputationalNotebook
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A virtual notebook environment used for literate programming.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="ComputationalNotebook">Jupyter</resourceType>

**Suggested Dublin Core Mapping:** InteractiveResource


.. _ConferencePaper:

ConferencePaper
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Article that is written with the goal of being accepted to a conference.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="ConferencePaper">Experience Report</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _ConferenceProceeding:

ConferenceProceeding
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Collection of academic papers published in the context of an academic conference.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="ConferenceProceeding">Annual Convention</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _DataPaper:

DataPaper
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A factual and objective publication with a focused intent to identify and describe specific data, sets of data, or data collections to facilitate discoverability.

**Examples and Usage Notes:** A data paper describes data provenance and methodologies used in the gathering, processing, organizing, and representing the data

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.17912/w2mw2d

**Suggested Dublin Core Mapping:** Text


.. _Dataset:

Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Data encoded in a defined structure.

**Examples and Usage Notes:** Data file or files

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.1594/pangaea.804876

**Suggested Dublin Core Mapping:** Dataset


.. _Dissertation:

Dissertation
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A written essay, treatise, or thesis, especially one written by a candidate for the degree of Doctor of Philosophy.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Dissertation">PhD thesis</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _Event:

Event
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A non-persistent, time-based occurrence.

**Examples and Usage Notes:** Descriptive information and/or content that is the basis for discovery of the purpose, location, duration, and responsible agents associated with an event such as a webcast or convention

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.7269/p3rn35sz

**Suggested Dublin Core Mapping:** Event


.. _Image:

Image
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A visual representation other than text.

**Examples and Usage Notes:** Digitised or born digital images, drawings or photographs

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.6083/m4qn65c5

**Suggested Dublin Core Mapping:** Image


.. _Instrument:

Instrument
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A device, tool or apparatus used to obtain, measure and/or analyze data.

**Examples and Usage Notes:** Note that this is meant to be the instrument instance, e.g., the individual physical device, not the digital description or design of an instrument.

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Instrument">Reflectometer</resourceType>

**Suggested Dublin Core Mapping:** N/A


.. _InteractiveResource:

InteractiveResource
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A resource requiring interaction from the user to be understood, executed, or experienced.

**Examples and Usage Notes:** Training modules, files that require use of a viewer (e.g., Flash), or query/response portals

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.7269/p3tb14tr

**Suggested Dublin Core Mapping:** InteractiveResource


.. _Journal:

Journal
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A scholarly publication consisting of articles that is published regularly throughout the year.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Journal"></resourceType>

**Suggested Dublin Core Mapping:** Text


.. _JournalArticle:

JournalArticle
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A written composition on a topic of interest, which forms a separate part of a journal.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="JournalArticle"></resourceType>

**Suggested Dublin Core Mapping:** Text


.. _Model:

Model
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An abstract, conceptual, graphical, mathematical or visualization model that represents empirical objects, phenomena, or physical processes.

**Examples and Usage Notes:** Modelled descriptions of, for example, different aspects of languages or a molecular biology reaction chain

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.5285/4d866cd2-c907-4ce2-b070-084ca9779dc2

**Suggested Dublin Core Mapping:** N/A


.. _OutputManagementPlan:

OutputManagementPlan
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A formal document that outlines how research outputs are to be handled both during a research project and after the project is completed.

**Examples and Usage Notes:** Includes data, software, and materials.

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="OutputManagementPlan">Data Management Plan</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _PeerReview:

PeerReview
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Evaluation of scientific, academic, or professional work by others working in the same field.

**Examples and Usage Notes:** https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.6084/m9.figshare.5742270

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="PeerReview">Scientific Article</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _PhysicalObject:

PhysicalObject
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A physical object or substance.

**Examples and Usage Notes:** Artifacts, specimens, material samples, and features-of-interest of any size. Note that digital representations of physical objects should use one of the other resourceTypeGeneral values.

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.7299/X78052RB

**Suggested Dublin Core Mapping:** PhysicalObject


.. _Preprint:

Preprint
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A version of a scholarly or scientific paper that precedes formal peer review and publication in a peer-reviewed scholarly or scientific journal.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Preprint">Research Paper</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _Project:

Project
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A planned endeavor or activity, frequently collaborative, intended to achieve a particular aim using allocated resources such as budget, time, and expertise.

**Examples and Usage Notes:** This resource type represents the project and includes research projects and studies. For a project deliverable or description of a project, use the corresponding resource type for the output—e.g., for a project report, dissertation, or study registration, use the resourceTypeGeneral “Report”, “Dissertation”, or “StudyRegistration” instead.

Examples:

.. code:: xml

  <resourceType resourceTypeGeneral="Project">Field season</resourceType>

.. code:: xml

  <resourceType resourceTypeGeneral="Project">Cohort study</resourceType>


**Suggested Dublin Core Mapping:** N/A


.. _Report:

Report
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A document that presents information in an organized format for a specific audience and purpose.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Report">Annual Report</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _Service:

Service
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An organized system of apparatus, appliances, staff, etc., for supplying some function(s) required by end users.

**Examples and Usage Notes:** Data management service, or long-term preservation service

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.21938/3I01ISNUCODNH1ZJBCVUWA

**Suggested Dublin Core Mapping:** Service


.. _Software:

Software
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A computer program other than a computational notebook, in either source code (text) or compiled form. Use this type for general software components supporting scholarly research. Use the "ComputationalNotebook" value for virtual notebooks.

**Examples and Usage Notes:** Software supporting scholarly research

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.4225/03/5954F738EE5AA

**Suggested Dublin Core Mapping:** Software


.. _Sound:

Sound
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A resource primarily intended to be heard.

**Examples and Usage Notes:** Audio recording

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.7282/T3J67F05

**Suggested Dublin Core Mapping:** Sound


.. _Standard:

Standard
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Something established by authority, custom, or general consent as a model, example, or point of reference.

**Examples and Usage Notes:**

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="Standard">Dublin Core</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _StudyRegistration:

StudyRegistration
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  A detailed, time-stamped description of a research plan, often openly shared in a registry or published in a journal before the study is conducted to lend accountability and transparency in the hypothesis generating and testing process.

**Examples and Usage Notes:** Includes pre-registrations, registered reports, and clinical trials. Study registrations are sometimes peer-reviewed and may include the hypothesis, expected results, study design, and/or analysis plan.

Example:

.. code:: xml

  <resourceType resourceTypeGeneral="StudyRegistration">Pre-registration</resourceType>

**Suggested Dublin Core Mapping:** Text


.. _Text:

Text
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A resource consisting primarily of words for reading that is not covered by any other textual resource type in this list.

**Examples and Usage Notes:**

Example: https://api.datacite.org/dois/application/vnd.datacite.datacite+xml/10.5682/9786065914018

**Suggested Dublin Core Mapping:** Text


.. _Workflow:

Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A structured series of steps which can be executed to produce a final outcome, allowing users a means to specify and enact their work in a more reproducible manner.

**Examples and Usage Notes:** Computational workflows involving sequential operations made on data by wrapped software and may be specified in a format belonging to a workflow management system, such as Taverna (http://www.taverna.org.uk/). [#f2]_

**Suggested Dublin Core Mapping:** N/A


.. _resourceTypeGeneral_Other:

Other
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** If selected, supply a value for ResourceType.

**Examples and Usage Notes:** ---

**Suggested Dublin Core Mapping:** ---


.. rubric:: Footnotes
.. [#f1] Where there is direct correspondence with the Dublin Core Metadata, DataCite definitions have borrowed liberally from the DCMI definitions. See: http://dublincore.org/documents/dcmi-terms/index.shtml
.. [#f2] An education module on workflows prepared by DataONE is available at http://www.dataone.org/sites/all/documents/L10_AnalysisWorkflows.pptx
