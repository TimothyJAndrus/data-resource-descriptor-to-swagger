# What is this?
This is a template repo that can be used to convert your Data Resource API descriptor files to swagger documentation by using this [library](https://github.com/brighthive/convert_descriptor_to_swagger).

At [BrightHive](https://brighthive.io) we use the [Data Resource API](https://github.com/brighthive/data-resource-api) to stand up a live database and API from a declarative document.

These documents are called descriptors. This repo will convert your descriptor to an [OpenAPI Specification 3.0 file](https://swagger.io/docs/specification/about/) that thoroughly documents your API.

# Instructions for using this
1. `git clone` this repo.

2. Ensure all of your API and table names are plural in your descriptor.

3. Add your descriptor files to the `descriptor` folder.

4. Run `pipenv install`.

5. Run `pipenv run python main.py`

6. A number of files will be produced; copy `swagger.json` and paste it into swaggerhub to make it pretty and convert it to YAML.

7. Clean up the swagger file. There will be a lot of errors.
