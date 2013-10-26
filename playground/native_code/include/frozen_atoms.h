#ifndef _PELE_FROZEN_ATOMS_H
#define _PELE_FROZEN_ATOMS_H

#include "array.h"
#include <vector>
#include <algorithm>
#include <set>
#include <assert.h>
#include "base_potential.h"

using std::vector;

namespace pele{
    /**
     * Class for converting to and from a reduced representation and back.
     * The full set of coordinates includes the mobile and frozen degrees of
     * freedom.  The reduced set of coordinates includes only the mobile
     * degrees of freedom.
     */
    class FrozenCoordsConverter{
        private:
            std::vector<double> const _reference_coords;
            std::vector<long int> _frozen_dof;
            std::vector<long int> _mobile_dof;
        public:
            FrozenCoordsConverter(Array<double> const & reference_coords, 
                    Array<long int> const & frozen_dof) :
                _reference_coords(reference_coords.begin(), reference_coords.end())
                //_frozen_dof(frozen_dof.begin(), frozen_dof.end())
            {
                //populate _frozen_dof after removing duplicates and sorting
                std::set<long int> frozenset(frozen_dof.begin(), frozen_dof.end());
                _frozen_dof = std::vector<long int>(frozenset.begin(), frozenset.end());
                std::sort(_frozen_dof.begin(), _frozen_dof.end());

                // do a sanity check
                if (_frozen_dof.size() > 0){
                    assert(_frozen_dof[_frozen_dof.size()-1] < ndof());
                }

                //populate _mobile_dof
                _mobile_dof = vector<long int>(ndof() - ndof_frozen());
                size_t imobile = 0;
                for (size_t i=0; i<_reference_coords.size(); ++i){
                    // if degree of freedom i is not in frozen, add it to _mobile_dof
                    if (frozenset.count(i) == 0){
                        _mobile_dof[imobile] = i;
                    }
                    ++imobile;
                }
                assert(imobile == _mobile_dof.size());

            }

            size_t ndof() const { return _reference_coords.size(); }
            size_t ndof_frozen() const { return _frozen_dof.size(); }
            size_t ndof_mobile() const { return _mobile_dof.size(); }

            /**
             * Return the reduced representation of the system.  i.e. return a
             * set of coordinates with the frozen degrees of freedom removed.
             */
            Array<double> get_reduced_coords(Array<double> const &full_coords){
                assert(full_coords.size() == ndof());
                Array<double> reduced_coords(ndof_mobile());
                for (size_t i=0; i < ndof_mobile(); ++i){
                    reduced_coords[i] = full_coords[_mobile_dof[i]];
                }
                return reduced_coords;
            }

            /**
             * Return the full representation of the system.  i.e. return a set
             * of coordinates with the frozen degrees of freedom added back in.
             */
            Array<double> get_full_coords(Array<double> const &reduced_coords){
                assert(reduced_coords.size() == ndof_mobile());
                // make a new array full_coords as a copy of _reference_coords.
                //Array<double> const a(_reference_coords); //wrap _reference_coords in an Array (returns error due to _reference_coords being const)
                ////Array<double> full_coords(a.copy());
                Array<double> full_coords(ndof());
                for (size_t i=0; i < ndof(); ++i){
                    full_coords[i] = _reference_coords[i];
                }
                // replace the mobile degrees of freedom with those in reduced_coords
                for (size_t i=0; i < ndof(); ++i){
                    full_coords[i] = reduced_coords[_mobile_dof[i]];
                }
                return full_coords;
            }

    };


    template<typename PotentialType>
    class FrozenPotentialWrapper : public BasePotential{
        protected:
            PotentialType *_underlying_potential;
            FrozenCoordsConverter _coords_converter;

            FrozenPotentialWrapper(PotentialType *potential, 
                    Array<double> &reference_coords, 
                    Array<long int> & frozen_dof) :
                _underlying_potential(potential),
                _coords_converter(reference_coords, frozen_dof) {}

        public:
            ~FrozenPotentialWrapper() 
            {
                if (_underlying_potential != NULL) { delete _underlying_potential; }
            }

            
            inline double get_energy(Array<double> reduced_coords) 
            {
                Array<double> full_coords(_coords_converter.get_full_coords(reduced_coords));
                return _underlying_potential->get_energy(full_coords);
            }

            inline double get_energy_gradient(Array<double> reduced_coords, Array<double> grad) 
            {
                Array<double> full_coords(_coords_converter.get_full_coords(reduced_coords));
                return _underlying_potential->get_energy_gradient(full_coords, grad);
            }
    };
}

#endif
