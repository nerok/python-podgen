# Modified work Copyright 2020, Thorben Dahl <thorben@sjostrom.no>
# See license.* for more details

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel --universal

clean: doc-clean
	@echo Removing binary files...
	@rm -f `find podgen -name '*.pyc'`
	@rm -f `find podgen -name '*.pyo'`
	@echo Removing source distribution files...
	@rm -rf dist/
	@rm -f MANIFEST

doc: doc-clean doc-html

doc-clean:
	@echo Removing docs...
	@make -C doc clean
	@rm -rf docs

doc-html:
	@echo 'Generating HTML'
	@make -C doc html
	@mkdir -p docs/html
	@echo 'Copying html to into docs dir'
	@cp -T -r doc/_build/html/ docs/html/

# Not supported
doc-man:
	@echo 'Generating manpage'
	@make -C doc man
	@mkdir -p docs/man
	@echo 'Copying manpage to into docs dir'
	@cp doc/_build/man/*.1 docs/man/

# Not supported
doc-latexpdf:
	@echo 'Generating pdf'
	@make -C doc latexpdf
	@mkdir -p docs/pdf
	@echo 'Copying pdf to into docs dir'
	@cp doc/_build/latex/*.pdf docs/pdf/

publish: sdist wheel
	twine upload dist/*

test:
	@python -m unittest podgen.tests.test_podcast podgen.tests.test_episode \
	  podgen.tests.test_person podgen.tests.test_media \
	  podgen.tests.test_util podgen.tests.test_category
	python -m podgen rss > /dev/null
